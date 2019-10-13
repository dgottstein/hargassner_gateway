import xml.etree.ElementTree as ET

def parse_header_information(filename):
    # Parse part of the xml file
    parsing_string = ""
    with open(filename) as xmlfile:
        start_found = False
        for line in xmlfile:
            beginstr = line.split("<DAQPRJ>")
            endstr = line.split("</DAQPRJ>")
            if len(beginstr) > 1:
                parsing_string += "<DAQPRJ>" + beginstr[1]
                start_found = True
            elif len(endstr) > 1:
                parsing_string += endstr[0] + "</DAQPRJ>"
                break
            elif start_found:
                parsing_string += line

    # Extract analog and digital channel information
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
