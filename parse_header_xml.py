import re
import xml.etree.ElementTree as ET
import json

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
    for analog_channel in channel_infos["analog"]:
        data = general_config["default_channel_config"].copy()
        data["title"] = general_config["default_channel_config"] + analog_channel[]
        output.append(data)
    return json.dumps(output)
