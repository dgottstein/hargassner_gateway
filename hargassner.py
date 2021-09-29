import binascii
from telnetlib import Telnet
import commentjson, json
import re
import xml.etree.ElementTree as ET
import uuid
import copy
#import pymysql
import mysql.connector
from mysql.connector.cursor import MySQLCursor
import time
import sys
import traceback


def parse_line(line_string, channel_infos):
    splitted = line_string.split(' ')
    parsed_data = {}
    
    for analog_key in channel_infos['analog']:
        tmp_data = channel_infos['analog'][analog_key]
        parsed_data[tmp_data['name']] = {'value': splitted[analog_key+1], 'unit': tmp_data['unit']}
    
    for digital_key in channel_infos['digital']:
        offset = digital_key + max(channel_infos['analog'].keys()) + 2
        tmp_infos = channel_infos['digital'][digital_key]
        for info_key in tmp_infos:
            value = 0
            if int.from_bytes(binascii.unhexlify(splitted[offset]), "big") & (1 << info_key):
                value = 1
            parsed_data[tmp_infos[info_key]['name']] = {'value': value, 'unit': 'bool'}
    return parsed_data


def compare_parsed_data(old_data, new_data):
    diff_data = {}
    if old_data != new_data:
        for key in new_data:
            if (key not in old_data) or (new_data[key] != old_data[key]):
                diff_data[key] = new_data[key]
    return diff_data


def parse_logfile(filename, channel_infos):
    old_data = {}
    with open(filename) as myfile:
        for line in myfile:
            new_data = parse_line(line, channel_infos)
            print(compare_parsed_data(old_data, new_data))
            print('\n', flush=True)
            old_data = new_data


def connect_and_parse(ip_address, channel_infos):
    old_data = {}
    with Telnet(ip_address, 23) as tn:
        while True:
            data_str = tn.read_until(b"\n").decode('ascii').strip()
            new_data = parse_line(data_str, channel_infos)
            print(compare_parsed_data(old_data, new_data))
            print('\n', flush=True)
            old_data = new_data


def connect_and_log_data(ip_address, channel_infos, channel_config, sql_connection):
    old_data = {}
    cursor = sql_connection.cursor()    # prepare a cursor object using cursor() method
    
    with Telnet(ip_address, 23) as tn:
        while True:
            new_data = {}
            try:
                data_str = tn.read_until(b"\n").decode('ascii').strip()
                timestamp = round(time.time() * 1000)
                #sql = []
                new_data = parse_line(data_str, channel_infos)
                diff_data = compare_parsed_data(old_data, new_data)
                for key, value in diff_data.items():
                    try:
                        uuid = channel_config[key]["vz"]["entities"]["uuid"]
                        sql_current = "INSERT INTO `data` (`channel_id`, `timestamp`, `value`) VALUES ((SELECT `id` FROM `entities` WHERE `uuid` LIKE '" + uuid + "' LIMIT 1), '" + str(timestamp) + "', '" + str(value["value"]) + "');"
                        try:
                            for result in cursor.execute(sql_current, multi=True):
                                if result.with_rows:
                                    print("Rows produced by statement '{}':".format(result.statement))
                                    print(result.fetchall(), flush=True)
                                elif result.rowcount != 1:
                                    print("Number of rows affected by statement '{}': {}".format(result.statement, result.rowcount), flush=True)
                                print("ID: {}".format(cursor.lastrowid), flush=True)
                        except RuntimeError:
                            pass    # TODO / FIXME: try to not raise StopIteration exception
                    except:
                        print("Unexpected sql error:", sys.exc_info(), sql_current, flush=True)
                        print(traceback.format_exc(), flush=True)
                    #try:
                    #    result = cursor.execute(sql_current)
                    #    sql_connection.commit()
                    #    try:
                    #        print(result, flush=True)
                    #    except RuntimeError:
                    #        pass    # TODO / FIXME: try to not raise StopIteration exception
                    #except:
                    #    print("Unexpected sql error:", sys.exc_info(), sql_current, flush=True)
                    #    print(traceback.format_exc(), flush=True)
                    #sql.append("INSERT INTO `data` (`channel_id`, `timestamp`, `value`) VALUES ((SELECT `id` FROM `entities` WHERE `uuid` LIKE '" + uuid + "' LIMIT 1), '" + str(timestamp) + "', '" + str(value["value"]) + "')")
                
                #if (len(sql) > 0):
                #    print((';\n'.join(sql)), flush=True)
                #    result = cursor.execute((';\n'.join(sql)), multi=True)
                #    sql_connection.commit()
                #    try:
                #        for record in result:
                #            print(record)
                #    except RuntimeError:
                #        pass    # TODO / FIXME: try to not raise StopIteration exception
            except:
                print("Unexpected error:", sys.exc_info(), flush=True)
                print(traceback.format_exc(), flush=True)
            
            old_data = new_data
    cursor.close()


def import_config_file(filename):
    with open(filename) as infile:
        d = commentjson.load(infile)
    return d


def parse_header_information(filename):
    # Extract xml part from DAQ file
    parsing_string = ""
    temp_string = ""
    with open(filename) as xmlfile:
        start_found = False
        for line in xmlfile:
            match = re.search(r'<DAQPRJ>.*?</DAQPRJ>', temp_string, re.DOTALL|re.IGNORECASE)
            if match != None:
                parsing_string = match.group(0)
                break
            temp_string += line

    # Parse and extract analog and digital channel information from xml part
    root = ET.fromstring(parsing_string)
    analog_channels = {};
    digital_channels = {};
    for child in root:
        for channel in child:
            if channel.tag == "CHANNEL":
                id = int(channel.attrib['id'])
                if child.tag == "ANALOG":
                    analog_channels[id] = channel.attrib
                    del analog_channels[id]['id']
                elif child.tag == "DIGITAL":
                    bit = int(channel.attrib['bit'])
                    if id not in digital_channels:
                        digital_channels[id] = {}
                    digital_channels[id][bit] = channel.attrib
                    del digital_channels[id][bit]['id']
                    del digital_channels[id][bit]['bit']

    return_dict = {"analog":analog_channels, "digital":digital_channels}
    return(return_dict)


def generate_channel_config(general_config, channel_infos, output_filename):
    output = {}
    for key, value in channel_infos["analog"].items():
        data = general_config["default_channel_config"].copy()
        data["type"] = "analog";
        data["position"] = key;
        data["vz"]["entities"]["uuid"] = str(uuid.uuid5(uuid.NAMESPACE_DNS, general_config["uuid_prefix"] + value["name"]))
        data["vz"]["properties"]["title"] = general_config["default_channel_config"]["title_prefix"] + value["name"]
        data["vz"]["properties"]["unit"] = value["unit"]
        del(data["title_prefix"])
        output[value["name"]] = copy.deepcopy(data)
    
    for key, value in channel_infos["digital"].items():
        for key2, value2 in value.items():
            data = general_config["default_channel_config"].copy()
            data["type"] = "digital"
            data["position"] = key
            data["bit"] = key2
            data["vz"]["entities"]["uuid"] = str(uuid.uuid5(uuid.NAMESPACE_DNS, general_config["uuid_prefix"] + value2["name"]))
            data["vz"]["properties"]["title"] = general_config["default_channel_config"]["title_prefix"] + value2["name"]
            del(data["title_prefix"])
            output[value2["name"]] = copy.deepcopy(data)
    
    output_str = json.dumps(output, sort_keys=True, indent=4)
    
    file_obj = open(output_filename,"w")
    file_obj.write(output_str)
    file_obj.close()
    
    return output_str


def create_vz_channels(general_config, channel_config, sql_connection):
    group_uuid = str(uuid.uuid5(uuid.NAMESPACE_DNS, general_config["uuid_prefix"] + general_config["group_title"]))
    cursor = sql_connection.cursor()    # prepare a cursor object using cursor() method
    
    sql = [];
    
    # add group and set properties
    sql.append("INSERT IGNORE INTO `entities` (`uuid`, `type`, `class`) VALUES ('" + group_uuid + "', 'group', 'aggregator')")
    sql.append("SET @group_id = LAST_INSERT_ID()")
    sql.append("INSERT IGNORE INTO `properties` (`entity_id`, `pkey`, `value`) VALUES (@group_id, 'public', '1'), (@group_id, 'title', '" + str(general_config["group_title"]) + "')")
    
    for value in channel_config:
        sql.append("INSERT IGNORE INTO `entities` (`uuid`, `type`, `class`) VALUES ('" + str(channel_config[value]["vz"]["entities"]["uuid"]) + "', '" + str(channel_config[value]["vz"]["entities"]["type"]) + "', '" + str(channel_config[value]["vz"]["entities"]["class"]) + "')")
        sql.append("SET @channel_id = LAST_INSERT_ID()")
        for prop_key, prop_val in channel_config[value]["vz"]["properties"].items():
            sql.append("INSERT IGNORE INTO `properties` (`entity_id`, `pkey`, `value`) VALUES (@channel_id, '" + str(prop_key) + "', '" + str(prop_val) + "')")
        sql.append("INSERT IGNORE INTO `entities_in_aggregator` (`parent_id`, `child_id`) VALUES (@group_id, @channel_id)")
    
    print('SQL:', flush=True)
    print(';\n'.join(sql), flush=True)
    
    results = cursor.execute((';\n'.join(sql)), multi=True)
    sql_connection.commit()
    
    cursor.close()

