import sys, traceback
from parse_header_xml import parse_header_information



expected_data = {'analog': {'0': {'id': '0', 'name': 'ZK', 'unit': ''}, '1': {'id': '1', 'name': 'O2', 'unit': '%'}, '2': {'id': '2', 'name': 'O2soll', 'unit': '%'}, '3': {'id': '3', 'name': 'TK', 'unit': '°C'}, '4': {'id': '4', 'name': 'TKsoll', 'unit': '°C'}, '5': {'id': '5', 'name': 'TRG', 'unit': '°C'}, '6': {'id': '6', 'name': 'SZist', 'unit': '%'}, '174': {'id': '174', 'name': 'FWS3 D', 'unit': 'l/min'}, '175': {'id': '175', 'name': 'FWS4 Anf.', 'unit': '°C'}, '176': {'id': '176', 'name': 'FWS4 Pumpe', 'unit': '%'}, '177': {'id': '177', 'name': 'FWS4 Leist', 'unit': 'kW'}, '178': {'id': '178', 'name': 'FWS4 T', 'unit': '°C'}, '179': {'id': '179', 'name': 'FWS4 D', 'unit': 'l/min'}, '180': {'id': '180', 'name': 'DiffReg2 S3', 'unit': '°C'}, '181': {'id': '181', 'name': 'DiffReg2 S4', 'unit': '°C'}}, 'digital': {'0': {'0': {'id': '0', 'bit': '0', 'name': 'Stb'}, '1': {'id': '0', 'bit': '1', 'name': 'Fuellstand'}, '3': {'id': '0', 'bit': '3', 'name': 'Es Rein Endl'}, '4': {'id': '0', 'bit': '4', 'name': 'HKPA'}, '5': {'id': '0', 'bit': '5', 'name': 'MAA'}, '6': {'id': '0', 'bit': '6', 'name': 'MAZ'}, '7': {'id': '0', 'bit': '7', 'name': 'HKP1'}, '8': {'id': '0', 'bit': '8', 'name': 'M1A'}}, '6': {'0': {'id': '6', 'bit': '0', 'name': 'gFlP'}, '1': {'id': '6', 'bit': '1', 'name': 'gFlM auf'}, '2': {'id': '6', 'bit': '2', 'name': 'gFlM zu'}, '4': {'id': '6', 'bit': '4', 'name': 'Spülung Aktiv'}}, '7': {'0': {'id': '7', 'bit': '0', 'name': 'DReg P1'}, '1': {'id': '7', 'bit': '1', 'name': 'DReg P2'}, '2': {'id': '7', 'bit': '2', 'name': 'DReg Mi auf'}, '3': {'id': '7', 'bit': '3', 'name': 'DReg Mi zu'}, '4': {'id': '7', 'bit': '4', 'name': 'Oel Out'}, '5': {'id': '7', 'bit': '5', 'name': 'DReg2 P1'}, '6': {'id': '7', 'bit': '6', 'name': 'DReg2 P2'}, '7': {'id': '7', 'bit': '7', 'name': 'DReg2 Mi auf'}, '8': {'id': '7', 'bit':'8', 'name': 'DReg2 Mi zu'}}}}
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



expected_data = {'analog': {'0': {'id': '0', 'name': 'ZK', 'unit': ''}, '1': {'id': '1', 'name': 'O2', 'unit': '%'}, '2': {'id': '2', 'name': 'O2soll', 'unit': '%'}, '3': {'id': '3', 'name': 'TK', 'unit': '°C'}, '178': {'id': '178', 'name': 'FWS4 T', 'unit': '°C'}, '179': {'id': '179', 'name': 'FWS4 D', 'unit': 'l/min'}, '180': {'id': '180', 'name': 'DiffReg2 S3', 'unit': '°C'}, '181': {'id': '181', 'name': 'DiffReg2 S4', 'unit': '°C'}}, 'digital': {'0': {'0': {'id': '0', 'bit': '0', 'name': 'Stb'}, '1': {'id': '0', 'bit': '1', 'name': 'Fuellstand'}, '3': {'id': '0', 'bit': '3', 'name': 'Es Rein Endl'}, '4': {'id': '0', 'bit': '4', 'name': 'HKPA'}, '5': {'id': '0', 'bit': '5', 'name': 'MAA'}, '6': {'id': '0', 'bit': '6', 'name': 'MAZ'}, '7': {'id': '0', 'bit': '7', 'name': 'HKP1'}, '8': {'id': '0', 'bit': '8', 'name': 'M1A'}, '9': {'id': '0', 'bit': '9', 'name': 'M1Z'}, '10': {'id':'0', 'bit': '10', 'name': 'HKP2'}, '11': {'id': '0', 'bit': '11', 'name': 'M2A'}, '12': {'id': '0', 'bit': '12', 'name': 'M2Z'}, '13': {'id': '0', 'bit': '13','name': 'Störung'}}, '7': {'4': {'id': '7', 'bit': '4', 'name': 'Oel Out'}, '5': {'id': '7', 'bit': '5', 'name': 'DReg2 P1'}, '6': {'id': '7', 'bit': '6', 'name': 'DReg2 P2'}, '7': {'id': '7', 'bit': '7', 'name': 'DReg2 Mi auf'}, '8': {'id': '7', 'bit': '8', 'name': 'DReg2 Mi zu'}}}}
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



expected_data = {'analog': {'0': {'id': '0', 'name': 'ZK', 'unit': ''}, '1': {'id': '1', 'name': 'O2', 'unit': '%'}, '2': {'id': '2', 'name': 'O2soll', 'unit': '%'}, '3': {'id': '3', 'name': 'TK', 'unit': '°C'}, '4': {'id': '4', 'name': 'TKsoll', 'unit': '°C'}, '5': {'id': '5', 'name': 'TRG', 'unit': '°C'}, '6': {'id': '6', 'name': 'SZist', 'unit': '%'}, '7': {'id': '7', 'name': 'SZsoll', 'unit': '%'}, '8': {'id': '8', 'name': 'Leistung', 'unit': '%'}, '179': {'id': '179', 'name': 'FWS4 D','unit': 'l/min'}, '180': {'id': '180', 'name': 'DiffReg2 S3', 'unit': '°C'}, '181': {'id': '181', 'name': 'DiffReg2 S4', 'unit': '°C'}}, 'digital': {'0': {'0':{'id': '0', 'bit': '0', 'name': 'Stb'}, '1': {'id': '0', 'bit': '1', 'name': 'Fuellstand'}, '3': {'id': '0', 'bit': '3', 'name': 'Es Rein Endl'}, '4': {'id': '0', 'bit': '4', 'name': 'HKPA'}, '5': {'id': '0', 'bit': '5', 'name': 'MAA'}, '6': {'id': '0', 'bit': '6', 'name': 'MAZ'}, '7': {'id': '0', 'bit': '7', 'name': 'HKP1'}, '8': {'id': '0', 'bit': '8', 'name': 'M1A'}, '9': {'id': '0', 'bit': '9', 'name': 'M1Z'}, '10': {'id': '0', 'bit': '10', 'name': 'HKP2'}, '11': {'id': '0', 'bit': '11', 'name': 'M2A'}, '12': {'id': '0', 'bit': '12', 'name': 'M2Z'},'13': {'id': '0', 'bit': '13', 'name': 'Störung'}}, '6': {'4': {'id': '6', 'bit': '4', 'name': 'Spülung Aktiv'}}, '7': {'0': {'id': '7', 'bit': '0', 'name': 'DReg P1'}, '1': {'id': '7', 'bit': '1', 'name': 'DReg P2'}, '2': {'id': '7', 'bit': '2', 'name': 'DReg Mi auf'}, '3': {'id': '7', 'bit': '3', 'name': 'DReg Mi zu'}, '4': {'id': '7', 'bit': '4', 'name': 'Oel Out'}, '5': {'id': '7', 'bit': '5', 'name': 'DReg2 P1'}, '6': {'id': '7', 'bit': '6', 'name': 'DReg2 P2'}, '7': {'id': '7', 'bit': '7', 'name': 'DReg2 Mi auf'}, '8': {'id': '7', 'bit': '8', 'name': 'DReg2 Mi zu'}}}}
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

