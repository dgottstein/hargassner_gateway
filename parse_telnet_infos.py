import binascii
from parse_header_xml import parse_header_information
import pprint

def parse_line(line_string, channel_information):
    splitted = line_string.split(' ')
    parsed_data = []
    
    for analog_key in channel_information['analog']:
        tmp_data = channel_information['analog'][analog_key]
        tmp_data['value'] = splitted[analog_key+1]
        parsed_data.append(tmp_data)
    
    for digital_key in channel_information['digital']:
        offset = digital_key + len(channel_information['analog']) + 1
        tmp_infos = channel_information['digital'][digital_key]
        for info_key in tmp_infos:
            tmp_infos[info_key]['unit'] = 'bool'
            if int.from_bytes(binascii.unhexlify(splitted[offset]), "big") & (1 << info_key):
                tmp_infos[info_key]['value'] = 1
            else:
                tmp_infos[info_key]['value'] = 0
            parsed_data.append(tmp_infos[info_key])
    return parsed_data



pp = pprint.PrettyPrinter(indent=4)

test_line = "pm 8 1.2 8.4 58 48 60 9 10 0 0 0 2 2 0 0 17 15 120 -20 120 -20 120 125 58 33 37 116.4 92.6 77 48 0 0 58 56 0 43 0 0 -5 50 0 0 100 100 8 0 47 73 1 0 -20 0 20 20 0 1 30 34 20 22 1 1 140 0 20 20 0 1 -20 0 20 20 0 1 -20 0 20 20 0 1 -20 0 20 20 0 1 -20 0 20 20 0 1 -20 0 0 56 0 0 -20 0 0 -20 0 0 0 0 0 34 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 140 -20 -20 -20 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -20 -20 0083 4000 0020 0000 0000 0160 0000 0000 "
channel_infos = parse_header_information("test\\xml\\Full.DAQ")
pp.pprint(parse_line(test_line, channel_infos))

