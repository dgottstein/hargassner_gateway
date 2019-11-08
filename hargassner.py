import binascii
from telnetlib import Telnet
import commentjson, json
import re
import xml.etree.ElementTree as ET
import uuid
import copy
#import pymysql
import mysql.connector


def parse_line(line_string, channel_information):
    splitted = line_string.split(' ')
    parsed_data = {}
    
    for analog_key in channel_information['analog']:
        tmp_data = channel_information['analog'][analog_key]
        parsed_data[tmp_data['name']] = {'value': splitted[analog_key+1], 'unit': tmp_data['unit']}
    
    for digital_key in channel_information['digital']:
        offset = digital_key + max(channel_information['analog'].keys()) + 2
        tmp_infos = channel_information['digital'][digital_key]
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


def parse_file(filename, channel_infos):
    old_data = {}
    with open(filename) as myfile:
        for line in myfile:
            new_data = parse_line(line, channel_infos)
            print(compare_parsed_data(old_data, new_data))
            print('\n')
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

def generate_channel_config(channel_infos, general_config, output_filename):
    output = []
    for key, value in channel_infos["analog"].items():
        data = general_config["default_channel_config"].copy()
        data["type"] = "analog";
        data["position"] = key;
        data["vz"]["entities"]["uuid"] = str(uuid.uuid5(uuid.NAMESPACE_DNS, general_config["uuid_prefix"] + value["name"]))
        data["vz"]["properties"]["title"] = general_config["default_channel_config"]["title_prefix"] + value["name"]
        data["vz"]["properties"]["unit"] = value["unit"]
        del(data["title_prefix"])
        output.append(copy.deepcopy(data))
    
    for key, value in channel_infos["digital"].items():
        for key2, value2 in value.items():
            data = general_config["default_channel_config"].copy()
            data["type"] = "digital"
            data["position"] = key
            data["bit"] = key2
            data["vz"]["entities"]["uuid"] = str(uuid.uuid5(uuid.NAMESPACE_DNS, general_config["uuid_prefix"] + value2["name"]))
            data["vz"]["properties"]["title"] = general_config["default_channel_config"]["title_prefix"] + value2["name"]
            del(data["title_prefix"])
            output.append(copy.deepcopy(data))
    
    output_str = json.dumps(output, sort_keys=True, indent=4)
    
    file_obj = open(output_filename,"w")
    file_obj.write(output_str)
    file_obj.close()
    
    return output_str

def create_vz_channels(general_config, sql_connection, channel_config_filename, ):
    group_uuid = str(uuid.uuid5(uuid.NAMESPACE_DNS, general_config["uuid_prefix"] + general_config["group_title"]))
    cursor = sql_connection.cursor()    # prepare a cursor object using cursor() method
    
    sql = [];
    
    # add group and set properties
    sql.append("INSERT INTO `entities` (`uuid`, `type`, `class`) VALUES (" + group_uuid + ", 'group', 'aggregator')")
    sql.append("SET @group_id = LAST_INSERT_ID()")
    sql.append("INSERT INTO `properties` (`entity_id`, `pkey`, `value`) VALUES (@group_id, 'public', '1'), (@group_id, 'title', '" + general_config["group_title"] + "')")
    
    with open(channel_config_filename) as infile:
        d = json.load(infile)
    
    for value in d:
        sql.append("INSERT INTO `entities` (`uuid`, `type`, `class`) VALUES ('" + value["vz"]["entities"]["uuid"] + "', '" + value["vz"]["entities"]["type"] + "', '" + value["vz"]["entities"]["class"] + "')")
        sql.append("SET @channel_id = LAST_INSERT_ID()")
        for prop_key, prop_val in value["vz"]["properties"].items():
            sql.append("INSERT INTO `properties` (`entity_id`, `pkey`, `value`) VALUES (@channel_id, '" + str(prop_key) + "', '" + str(prop_val) + "')")
        sql.append("INSERT INTO `entities_in_aggregator` (`parent_id`, `child_id`) VALUES (@group_id, @channel_id)")
    
    with sql_connection.cursor() as cursor:
        cursor.execute(('; '.join(sql)), multi=True)
    sql_connection.commit()

# Open database connection
db = pymysql.connect("homeserver","volkszaehler","meinPasswort","volkszaehler" )
db2 = mysql.connector.connect(host='homeserver', database='volkszaehler', user='volkszaehler', password='meinPasswort', use_pure=True) # use pure Python implementation
