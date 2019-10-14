import sys, traceback
from parse_header_xml import parse_header_information



expected_data = {'analog': [{'id': '0', 'name': 'ZK', 'unit': ''}, {'id': '1', 'name': 'O2', 'unit': '%'}, {'id': '2', 'name': 'O2soll', 'unit': '%'}, {'id': '3', 'name': 'TK', 'unit': '°C'}, {'id': '4', 'name': 'TKsoll', 'unit': '°C'}, {'id': '5', 'name': 'TRG', 'unit': '°C'}, {'id': '6', 'name': 'SZist', 'unit': '%'}, {'id': '174','name': 'FWS3 D', 'unit': 'l/min'}, {'id': '175', 'name': 'FWS4 Anf.', 'unit': '°C'}, {'id': '176', 'name': 'FWS4 Pumpe', 'unit': '%'}, {'id': '177', 'name': 'FWS4 Leist', 'unit': 'kW'}, {'id': '178', 'name': 'FWS4 T', 'unit': '°C'}, {'id': '179', 'name': 'FWS4 D', 'unit': 'l/min'}, {'id': '180', 'name': 'DiffReg2 S3', 'unit': '°C'}, {'id': '181', 'name': 'DiffReg2 S4', 'unit': '°C'}], 'digital':[{'id': '0', 'bit': '0', 'name': 'Stb'}, {'id': '0', 'bit': '1', 'name': 'Fuellstand'}, {'id': '0', 'bit': '3', 'name': 'Es Rein Endl'}, {'id': '0', 'bit': '4', 'name': 'HKPA'}, {'id': '0', 'bit': '5', 'name': 'MAA'}, {'id': '0', 'bit': '6', 'name': 'MAZ'}, {'id': '0', 'bit': '7', 'name': 'HKP1'}, {'id': '0', 'bit': '8', 'name': 'M1A'}, {'id': '6', 'bit': '0', 'name': 'gFlP'}, {'id': '6', 'bit': '1', 'name': 'gFlM auf'}, {'id': '6', 'bit': '2', 'name': 'gFlM zu'}, {'id': '6', 'bit': '4', 'name': 'Spülung Aktiv'}, {'id': '7', 'bit': '0', 'name': 'DReg P1'}, {'id': '7', 'bit': '1', 'name': 'DReg P2'}, {'id': '7', 'bit': '2', 'name': 'DReg Mi auf'}, {'id': '7', 'bit': '3', 'name': 'DReg Mi zu'}, {'id': '7', 'bit': '4', 'name': 'Oel Out'}, {'id': '7', 'bit': '5', 'name': 'DReg2 P1'}, {'id': '7', 'bit': '6', 'name': 'DReg2 P2'}, {'id': '7', 'bit': '7', 'name': 'DReg2 Mi auf'}, {'id': '7', 'bit': '8', 'name': 'DReg2 Mi zu'}]}
print("Testing 'parse_header_information(\"test\\xml\\DAQ00000.xml\")'")
try:
    data = parse_header_information("test\\xml\\DAQ00000.xml")
    if data == expected_data:
        print("Passed.");
    else:
        print("Failed! Parsed data:")
        print(data)
        print("Should be:")
        print(expected_data)
except:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print("Unexpected error:", exc_type)
    traceback.print_tb(exc_traceback, limit=2, file=sys.stdout)
print("\n")



expected_data = {'analog': [{'id': '0', 'name': 'ZK', 'unit': ''}, {'id': '1', 'name': 'O2', 'unit': '%'}, {'id': '2', 'name': 'O2soll', 'unit': '%'}, {'id': '3', 'name': 'TK',
 'unit': '°C'}, {'id': '178', 'name': 'FWS4 T', 'unit': '°C'}, {'id': '179', 'name': 'FWS4 D', 'unit': 'l/min'}, {'id': '180', 'name': 'DiffReg2 S3', 'unit': '°C'}, {'id': '181', 'name': 'DiffReg2 S4', 'unit': '°C'}], 'digital': [{'id': '0', 'bit': '0', 'name': 'Stb'}, {'id': '0', 'bit': '1', 'name': 'Fuellstand'}, {'id': '0', 'bit': '3', 'name': 'Es Rein Endl'}, {'id': '0', 'bit': '4', 'name': 'HKPA'}, {'id': '0', 'bit': '5', 'name': 'MAA'}, {'id': '0', 'bit': '6', 'name': 'MAZ'}, {'id': '0', 'bit': '7', 'name': 'HKP1'}, {'id': '0', 'bit': '8', 'name':'M1A'}, {'id': '0', 'bit': '9', 'name': 'M1Z'}, {'id': '0', 'bit': '10', 'name': 'HKP2'}, {'id': '0', 'bit': '11', 'name': 'M2A'}, {'id': '0', 'bit': '12', 'name': 'M2Z'}, {'id': '0', 'bit': '13', 'name': 'Störung'}, {'id': '7', 'bit': '4', 'name': 'Oel Out'}, {'id': '7', 'bit': '5', 'name': 'DReg2 P1'}, {'id': '7', 'bit': '6', 'name': 'DReg2 P2'}, {'id': '7', 'bit': '7', 'name': 'DReg2 Mi auf'},{'id': '7', 'bit': '8', 'name': 'DReg2 Mi zu'}]}
print("Testing 'parse_header_information(\"test\\xml\\DAQ00000.DAQ\")'")
try:
    data = parse_header_information("test\\xml\\DAQ00000.DAQ")
    if data == expected_data:
        print("Passed.");
    else:
        print("Failed! Parsed data:")
        print(data)
        print("Should be:")
        print(expected_data)
except:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print("Unexpected error:", exc_type)
    traceback.print_tb(exc_traceback, limit=2, file=sys.stdout)
print("\n")



expected_data = {'analog': [{'id': '0', 'name': 'ZK', 'unit': ''}, {'id': '1', 'name': 'O2', 'unit': '%'}, {'id': '2', 'name': 'O2soll', 'unit': '%'}, {'id': '3', 'name': 'TK', 'unit': '°C'}, {'id': '4', 'name': 'TKsoll', 'unit': '°C'}, {'id': '5', 'name': 'TRG', 'unit': '°C'}, {'id': '6', 'name': 'SZist', 'unit': '%'}, {'id': '7', 'name': 'SZsoll', 'unit': '%'}, {'id': '8', 'name': 'Leistung', 'unit': '%'}, {'id': '179', 'name': 'FWS4 D', 'unit': 'l/min'}, {'id': '180', 'name': 'DiffReg2 S3', 'unit': '°C'}, {'id': '181', 'name': 'DiffReg2 S4', 'unit': '°C'}], 'digital': [{'id': '0', 'bit': '0', 'name': 'Stb'}, {'id': '0', 'bit': '1', 'name': 'Fuellstand'}, {'id': '0', 'bit': '3', 'name': 'Es Rein Endl'}, {'id': '0', 'bit': '4', 'name': 'HKPA'}, {'id': '0', 'bit': '5', 'name': 'MAA'}, {'id': '0', 'bit': '6', 'name': 'MAZ'}, {'id': '0', 'bit': '7', 'name': 'HKP1'}, {'id': '0', 'bit':'8', 'name': 'M1A'}, {'id': '0', 'bit': '9', 'name': 'M1Z'}, {'id': '0', 'bit':'10', 'name': 'HKP2'}, {'id': '0', 'bit': '11', 'name': 'M2A'}, {'id': '0', 'bit': '12', 'name': 'M2Z'}, {'id': '0', 'bit': '13', 'name': 'Störung'}, {'id': '6', 'bit': '4', 'name': 'Spülung Aktiv'}, {'id': '7', 'bit': '0', 'name': 'DReg P1'}, {'id': '7', 'bit': '1', 'name': 'DReg P2'}, {'id': '7', 'bit': '2', 'name':'DReg Mi auf'}, {'id': '7', 'bit': '3', 'name': 'DReg Mi zu'}, {'id': '7', 'bit': '4', 'name': 'Oel Out'}, {'id': '7', 'bit': '5', 'name': 'DReg2 P1'}, {'id': '7', 'bit': '6', 'name': 'DReg2 P2'}, {'id': '7', 'bit': '7', 'name': 'DReg2 Mi auf'}, {'id': '7', 'bit': '8', 'name': 'DReg2 Mi zu'}]}
print("Testing 'parse_header_information(\"test\\xml\\DAQ00001.DAQ\")'")
try:
    data = parse_header_information("test\\xml\\DAQ00001.DAQ")
    if data == expected_data:
        print("Passed.");
    else:
        print("Failed! Parsed data:")
        print(data)
        print("Should be:")
        print(expected_data)
except:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print("Unexpected error:", exc_type)
    traceback.print_tb(exc_traceback, limit=2, file=sys.stdout)
print("\n")

