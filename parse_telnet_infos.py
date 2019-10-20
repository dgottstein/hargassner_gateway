import binascii
from parse_header_xml import parse_header_information
from telnetlib import Telnet

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

