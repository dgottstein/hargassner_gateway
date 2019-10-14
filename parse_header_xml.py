import re
import xml.etree.ElementTree as ET

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
    analog_channels = [];
    digital_channels = [];
    for child in root:
        for analogchild in child:
            if analogchild.tag == "CHANNEL":
                if child.tag == "ANALOG":
                    analog_channels.append(analogchild.attrib)
                elif child.tag == "DIGITAL":
                    digital_channels.append(analogchild.attrib)

    return_dict = {"analog":analog_channels, "digital":digital_channels}
    return(return_dict)
