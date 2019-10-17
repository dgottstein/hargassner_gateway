import binascii
from parse_header_xml import parse_header_information

def parse_line(line_string, channel_information):
    splitted = line_string.split(' ')
    parsed_data = []
    
    for analog_key in channel_information['analog']:
        tmp_data = channel_information['analog'][analog_key]
        tmp_data['value'] = splitted[analog_key+1]
        parsed_data.append(tmp_data)
    
    for digital_key in channel_information['digital']:
        offset = digital_key + max(channel_information['analog'].keys()) + 2
        tmp_infos = channel_information['digital'][digital_key]
        for info_key in tmp_infos:
            tmp_infos[info_key]['unit'] = 'bool'
            if int.from_bytes(binascii.unhexlify(splitted[offset]), "big") & (1 << info_key):
                tmp_infos[info_key]['value'] = 1
            else:
                tmp_infos[info_key]['value'] = 0
            parsed_data.append(tmp_infos[info_key])
    return parsed_data

