import hargassner
import sys, traceback




expected_data = {'analog': {'0': {'id': '0', 'name': 'ZK', 'unit': ''}, '1': {'id': '1', 'name': 'O2', 'unit': '%'}, '2': {'id': '2', 'name': 'O2soll', 'unit': '%'}, '3': {'id': '3', 'name': 'TK', 'unit': '°C'}, '4': {'id': '4', 'name': 'TKsoll', 'unit': '°C'}, '5': {'id': '5', 'name': 'TRG', 'unit': '°C'}, '6': {'id': '6', 'name': 'SZist', 'unit': '%'}, '174': {'id': '174', 'name': 'FWS3 D', 'unit': 'l/min'}, '175': {'id': '175', 'name': 'FWS4 Anf.', 'unit': '°C'}, '176': {'id': '176', 'name': 'FWS4 Pumpe', 'unit': '%'}, '177': {'id': '177', 'name': 'FWS4 Leist', 'unit': 'kW'}, '178': {'id': '178', 'name': 'FWS4 T', 'unit': '°C'}, '179': {'id': '179', 'name': 'FWS4 D', 'unit': 'l/min'}, '180': {'id': '180', 'name': 'DiffReg2 S3', 'unit': '°C'}, '181': {'id': '181', 'name': 'DiffReg2 S4', 'unit': '°C'}}, 'digital': {'0': {'0': {'id': '0', 'bit': '0', 'name': 'Stb'}, '1': {'id': '0', 'bit': '1', 'name': 'Fuellstand'}, '3': {'id': '0', 'bit': '3', 'name': 'Es Rein Endl'}, '4': {'id': '0', 'bit': '4', 'name': 'HKPA'}, '5': {'id': '0', 'bit': '5', 'name': 'MAA'}, '6': {'id': '0', 'bit': '6', 'name': 'MAZ'}, '7': {'id': '0', 'bit': '7', 'name': 'HKP1'}, '8': {'id': '0', 'bit': '8', 'name': 'M1A'}}, '6': {'0': {'id': '6', 'bit': '0', 'name': 'gFlP'}, '1': {'id': '6', 'bit': '1', 'name': 'gFlM auf'}, '2': {'id': '6', 'bit': '2', 'name': 'gFlM zu'}, '4': {'id': '6', 'bit': '4', 'name': 'Spülung Aktiv'}}, '7': {'0': {'id': '7', 'bit': '0', 'name': 'DReg P1'}, '1': {'id': '7', 'bit': '1', 'name': 'DReg P2'}, '2': {'id': '7', 'bit': '2', 'name': 'DReg Mi auf'}, '3': {'id': '7', 'bit': '3', 'name': 'DReg Mi zu'}, '4': {'id': '7', 'bit': '4', 'name': 'Oel Out'}, '5': {'id': '7', 'bit': '5', 'name': 'DReg2 P1'}, '6': {'id': '7', 'bit': '6', 'name': 'DReg2 P2'}, '7': {'id': '7', 'bit': '7', 'name': 'DReg2 Mi auf'}, '8': {'id': '7', 'bit':'8', 'name': 'DReg2 Mi zu'}}}}
print("Testing parse_header_information(\"test\\xml\\DAQ00000.xml\")")
try:
    data = hargassner.parse_header_information("test\\xml\\DAQ00000.xml")
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
print("Testing parse_header_information(\"test\\xml\\DAQ00000.DAQ\")")
try:
    data = hargassner.parse_header_information("test\\xml\\DAQ00000.DAQ")
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
print("Testing parse_header_information(\"test\\xml\\DAQ00001.DAQ\")")
try:
    data = hargassner.parse_header_information("test\\xml\\DAQ00001.DAQ")
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





test_line1 = "pm 8 1.2 8.4 58 48 60 9 10 0 0 0 2 2 0 0 17 15 120 -20 120 -20 120 125 58 33 37 116.4 92.6 77 48 0 0 58 56 0 43 0 0 -5 50 0 0 100 100 8 0 47 73 1 0 -20 0 20 20 0 1 30 34 20 22 1 1 140 0 20 20 0 1 -20 0 20 20 0 1 -20 0 20 20 0 1 -20 0 20 20 0 1 -20 0 20 20 0 1 -20 0 0 56 0 0 -20 0 0 -20 0 0 0 0 0 34 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 140 -20 -20 -20 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -20 -20 0083 4000 0020 0000 0000 0160 0000 0000 "
test_line2 = "pm 8 1.2 8.4 58 48 60 9 10 0 0 0 2 2 0 0 17 15 120 -20 110 -20 120 125 58 33 37 116.4 92.6 77 48 0 0 58 56 0 43 0 0 -5 50 0 0 100 100 8 0 47 73 0 0 -20 0 20 20 0 1 30 34 20 22 1 1 140 0 20 20 0 1 -20 0 20 20 0 1 -20 0 20 20 0 1 -20 0 20 20 0 1 -20 0 20 20 0 1 -20 0 0 56 0 0 -20 0 0 -20 0 0 0 0 0 34 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 140 -20 -20 -20 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -20 -20 0083 4000 0020 0000 0000 0060 0000 0000 "
full_channel_infos = hargassner.parse_header_information("test\\xml\\Full.DAQ")
partial_channel_infos = hargassner.parse_header_information("test\\xml\\DAQ00000.xml")


print("Testing parse_line(test_line1, full_channel_infos)")
expected_result = {'ZK': {'value': '8', 'unit': ''}, 'O2': {'value': '1.2', 'unit': '%'}, 'O2soll': {'value': '8.4', 'unit': '%'}, 'TK': {'value': '58', 'unit': '°C'}, 'TKsoll': {'value': '48', 'unit': '°C'}, 'TRG': {'value': '60', 'unit': '°C'}, 'SZist': {'value': '9', 'unit': '%'}, 'SZsoll': {'value': '10', 'unit': '%'}, 'Leistung': {'value': '0', 'unit': '%'}, 'ESsoll': {'value': '0', 'unit': '%'}, 'I Es': {'value': '0', 'unit': 'mA'}, 'I Ra': {'value': '2', 'unit': 'mA'}, 'I Aa': {'value': '2', 'unit': 'mA'}, 'I Sr': {'value': '0', 'unit': 'mA'}, 'I Rein': {'value': '0', 'unit': 'mA'}, 'Taus': {'value': '17', 'unit': '°C'}, 'TA Gem.': {'value': '15', 'unit': '°C'}, 'TPo': {'value': '120', 'unit': '°C'}, 'TPmo': {'value': '-20', 'unit': '°C'}, 'TPm': {'value': '120', 'unit': '°C'}, 'TPmu': {'value': '-20', 'unit': '°C'}, 'TPu': {'value': '120', 'unit': '°C'}, 'TFW': {'value': '125', 'unit': '°C'}, 'TRL': {'value': '58', 'unit': '°C'}, 'TRLsoll': {'value': '33', 'unit': '°C'}, 'Tplat': {'value': '37', 'unit': '°C'}, 'BRT': {'value': '116.4', 'unit': '°C'}, 'Regler K': {'value': '92.6', 'unit': ''}, 'KeBrstScale': {'value': '77', 'unit': '%'}, 'ESRegler': {'value': '48', 'unit': '%'}, 'BLDC_ES ist': {'value': '0', 'unit': 'rpm'}, 'BLDC_ES soll': {'value': '0', 'unit': 'rpm'}, 'LZ ES seit Füll.': {'value': '58', 'unit': 'Min'}, 'LZ ES seit Ent.': {'value': '56', 'unit': 'Min'}, 'Anzahl Entasch.': {'value': '0', 'unit': ''}, 'Anzahl SR Beweg.': {'value': '43', 'unit': ''}, 'Heiz P Lambda': {'value': '0', 'unit': 'W'}, 'Heiz U Lambda': {'value': '0', 'unit': 'V'}, 'Heiz I Lambda': {'value': '-5', 'unit': 'mA'}, 'Sens U Lambda': {'value': '50', 'unit': 'mV'}, 'PuffZustand': {'value': '0', 'unit': ''}, 'Puffer_soll': {'value': '0', 'unit': '°C'}, 'Puff Füllgrad': {'value': '100', 'unit': '%'}, 'max.Leist.P3F.HT': {'value': '100', 'unit': '%'}, 'Spreizung': {'value': '8', 'unit': '°C'}, 'AIN17': {'value': '0', 'unit': 'V'}, 'Lagerstand': {'value': '47', 'unit': 'kg'}, 'Verbrauchszähler': {'value': '73', 'unit': 'kg'}, 'UsePos': {'value': '1', 'unit': ''}, 'Störungs Nr': {'value': '0', 'unit': ''}, 'TVL_A': {'value': '-20', 'unit': '°C'}, 'TVLs_A': {'value': '0', 'unit': '°C'}, 'TRA_A': {'value': '20', 'unit': '°C'}, 'TRs_A': {'value': '20', 'unit': '°C'}, 'HKZustand_A': {'value': '0', 'unit': ''}, 'FRA Zustand': {'value': '1', 'unit': ''}, 'TVL_1': {'value': '30', 'unit': '°C'}, 'TVLs_1': {'value': '34', 'unit': '°C'}, 'TRA_1': {'value': '20', 'unit': '°C'}, 'TRs_1': {'value': '22', 'unit': '°C'}, 'HKZustand_1': {'value': '1', 'unit': ''}, 'FR1 Zustand': {'value': '1', 'unit': ''}, 'TVL_2': {'value': '140', 'unit': '°C'}, 'TVLs_2': {'value': '0', 'unit': '°C'}, 'TRA_2': {'value': '20', 'unit': '°C'}, 'TRs_2': {'value': '20', 'unit': '°C'}, 'HKZustand_2': {'value': '0', 'unit': ''}, 'FR2 Zustand': {'value': '1', 'unit': ''}, 'TVL_3': {'value': '-20', 'unit': '°C'}, 'TVLs_3': {'value': '0', 'unit': '°C'}, 'TRA_3': {'value': '20', 'unit': '°C'}, 'TRs_3': {'value': '20', 'unit': '°C'}, 'HKZustand_3': {'value': '0', 'unit': ''}, 'FR3 Zustand': {'value': '1', 'unit': ''}, 'TVL_4': {'value': '-20', 'unit': '°C'}, 'TVLs_4': {'value': '0', 'unit': '°C'}, 'TRA_4': {'value': '20', 'unit': '°C'}, 'TRs_4': {'value': '20', 'unit': '°C'}, 'HKZustand_4': {'value': '0', 'unit': ''}, 'FR4 Zustand': {'value': '1', 'unit': ''}, 'TVL_5': {'value': '-20', 'unit': '°C'}, 'TVLs_5': {'value': '0', 'unit': '°C'}, 'TRA_5': {'value': '20', 'unit': '°C'}, 'TRs_5': {'value': '20', 'unit': '°C'}, 'HKZustand_5': {'value': '0', 'unit': ''}, 'FR5 Zustand': {'value': '1', 'unit': ''}, 'TVL_6': {'value': '-20', 'unit': '°C'}, 'TVLs_6': {'value': '0', 'unit': '°C'}, 'TRA_6': {'value': '20', 'unit': '°C'}, 'TRs_6': {'value': '20', 'unit': '°C'}, 'HKZustand_6': {'value': '0', 'unit': ''}, 'FR6 Zustand': {'value': '1', 'unit': ''}, 'TBA': {'value': '-20', 'unit': '°C'}, 'TBs_A': {'value': '0', 'unit': '°C'}, 'BoiZustand_A': {'value': '0', 'unit': ''}, 'TB1': {'value': '56', 'unit': '°C'}, 'TBs_1': {'value': '0', 'unit': '°C'}, 'BoiZustand_1': {'value': '0', 'unit': ''}, 'TB2': {'value': '-20', 'unit': '°C'}, 'TBs_2': {'value': '0', 'unit': '°C'}, 'BoiZustand_2': {'value': '0', 'unit': ''}, 'TB3': {'value': '-20', 'unit': '°C'}, 'TBs_3': {'value': '0', 'unit': '°C'}, 'BoiZustand_3': {'value': '0', 'unit': ''}, 'Ext.HK Soll': {'value': '0', 'unit': ''}, 'Ext.HK Soll_2': {'value': '0', 'unit': ''}, 'Ext.HK Soll_3': {'value': '0', 'unit': ''}, 'Höchste Anf': {'value': '34', 'unit': ''}, 'Anf. HKR0': {'value': '0', 'unit': '°C'}, 'Anf. HKR1': {'value': '0', 'unit': '°C'}, 'Anf. HKR2': {'value': '0', 'unit': '°C'}, 'Anf. HKR3': {'value': '0', 'unit': '°C'}, 'Anf. HKR4': {'value': '0', 'unit': '°C'}, 'Anf. HKR5': {'value': '0', 'unit': '°C'}, 'Anf. HKR6': {'value': '0', 'unit': '°C'}, 'Anf. HKR7': {'value': '0', 'unit': '°C'}, 'Anf. HKR8': {'value': '0', 'unit': '°C'}, 'Anf. HKR9': {'value': '0', 'unit': '°C'}, 'Anf. HKR10': {'value': '0', 'unit': '°C'}, 'Anf. HKR11': {'value': '0', 'unit': '°C'}, 'Anf. HKR12': {'value': '0', 'unit': '°C'}, 'Anf. HKR13': {'value': '0', 'unit': '°C'}, 'Anf. HKR14': {'value': '0', 'unit': '°C'}, 'Anf. HKR15': {'value': '0', 'unit': '°C'}, 'KaskSollTmp_1': {'value': '0', 'unit': '°C'}, 'KaskSollTmp_2': {'value': '0', 'unit': '°C'}, 'KaskSollTmp_3': {'value': '0', 'unit': '°C'}, 'KaskSollTmp_4': {'value': '0', 'unit': '°C'}, 'KaskIstTmp_1': {'value': '0', 'unit': '°C'}, 'KaskIstTmp_2': {'value': '0', 'unit': '°C'}, 'KaskIstTmp_3': {'value': '0', 'unit': '°C'}, 'KaskIstTmp_4': {'value': '0', 'unit': '°C'}, 'T Spülung': {'value': '140', 'unit': '°C'}, 'DiffReg S1': {'value': '-20', 'unit': '°C'}, 'DiffReg S2': {'value': '-20', 'unit': '°C'}, 'TVG': {'value': '-20', 'unit': '°C'}, 'WMZ_1_TVL': {'value': '-1', 'unit': '°C'}, 'WMZ_1_TRL': {'value': '-1', 'unit': '°C'}, 'WMZ_1_PWR': {'value': '-1', 'unit': 'kW'}, 'WMZ_1_FLOW': {'value': '-1', 'unit': 'l/h'}, 'WMZ_2_TVL': {'value': '-1', 'unit': '°C'}, 'WMZ_2_TRL': {'value': '-1', 'unit': '°C'}, 'WMZ_2_PWR': {'value': '-1', 'unit': 'kW'}, 'WMZ_2_FLOW': {'value': '-1', 'unit': 'l/h'}, 'WMZ_3_TVL': {'value': '-1', 'unit': '°C'}, 'WMZ_3_TRL': {'value': '-1', 'unit': '°C'}, 'WMZ_3_PWR': {'value': '-1', 'unit': 'kW'}, 'WMZ_3_FLOW': {'value': '-1', 'unit': 'l/h'}, 'WMZ_4_TVL': {'value': '-1', 'unit': '°C'}, 'WMZ_4_TRL': {'value': '-1', 'unit': '°C'}, 'WMZ_4_PWR': {'value': '-1', 'unit': 'kW'}, 'WMZ_4_FLOW': {'value': '-1', 'unit': 'l/h'}, 'WMZ_5_TVL': {'value': '-1', 'unit': '°C'}, 'WMZ_5_TRL': {'value': '-1', 'unit': '°C'}, 'WMZ_5_PWR': {'value': '-1', 'unit': 'kW'}, 'WMZ_5_FLOW': {'value': '-1', 'unit': 'l/h'}, 'WMZ_6_TVL': {'value': '-1', 'unit': '°C'}, 'WMZ_6_TRL': {'value': '-1', 'unit': '°C'}, 'WMZ_6_PWR': {'value': '-1', 'unit': 'kW'}, 'WMZ_6_FLOW': {'value': '-1', 'unit': 'l/h'}, 'FWS1 Anf.': {'value': '0', 'unit': '°C'}, 'FWS1 Pumpe': {'value': '0', 'unit': '%'}, 'FWS1 Leist': {'value': '0', 'unit': 'kW'}, 'FWS1 T': {'value': '0', 'unit': '°C'}, 'FWS1 D': {'value': '0', 'unit': 'l/min'}, 'FWS2 Anf.': {'value': '0', 'unit': '°C'}, 'FWS2 Pumpe': {'value': '0', 'unit': '%'}, 'FWS2 Leist': {'value': '0', 'unit': 'kW'}, 'FWS2 T': {'value': '0', 'unit': '°C'}, 'FWS2 D': {'value': '0', 'unit': 'l/min'}, 'FWS3 Anf.': {'value': '0', 'unit': '°C'}, 'FWS3 Pumpe': {'value': '0', 'unit': '%'}, 'FWS3 Leist': {'value': '0', 'unit': 'kW'}, 'FWS3 T': {'value': '0', 'unit': '°C'}, 'FWS3 D': {'value': '0', 'unit': 'l/min'}, 'FWS4 Anf.': {'value': '0', 'unit': '°C'}, 'FWS4 Pumpe': {'value': '0', 'unit': '%'}, 'FWS4 Leist': {'value': '0', 'unit': 'kW'}, 'FWS4 T': {'value': '0', 'unit': '°C'}, 'FWS4 D': {'value': '0', 'unit': 'l/min'}, 'DiffReg2 S3': {'value': '-20', 'unit': '°C'}, 'DiffReg2 S4': {'value': '-20', 'unit': '°C'}, 'Stb': {'value': 1, 'unit': 'bool'}, 'Fuellstand': {'value': 1, 'unit': 'bool'}, 'Es Rein Endl': {'value': 0, 'unit': 'bool'}, 'HKPA': {'value': 0, 'unit': 'bool'}, 'MAA': {'value': 0, 'unit': 'bool'}, 'MAZ': {'value': 0, 'unit': 'bool'}, 'HKP1': {'value': 1, 'unit': 'bool'}, 'M1A': {'value': 0, 'unit': 'bool'}, 'M1Z': {'value': 0, 'unit': 'bool'}, 'HKP2': {'value': 0, 'unit': 'bool'}, 'M2A': {'value': 0, 'unit': 'bool'}, 'M2Z': {'value': 0, 'unit': 'bool'}, 'Störung': {'value': 0, 'unit': 'bool'}, 'L Heiz.': {'value': 0, 'unit': 'bool'}, 'Z Heiz.': {'value': 0, 'unit': 'bool'}, 'Z Geb.': {'value': 0, 'unit': 'bool'}, 'AA Run': {'value': 0, 'unit': 'bool'}, 'AA Dir': {'value': 0, 'unit': 'bool'}, 'ES Run': {'value': 0, 'unit': 'bool'}, 'ES Dir': {'value': 0, 'unit': 'bool'}, 'AS Saug': {'value': 0, 'unit': 'bool'}, 'AS RA Run': {'value': 0, 'unit': 'bool'}, 'AS RA Dir': {'value': 0, 'unit': 'bool'}, 'Rein En': {'value': 0, 'unit': 'bool'}, 'Rein Run': {'value': 0, 'unit': 'bool'}, 'RLm_auf': {'value': 0, 'unit': 'bool'}, 'RLm_zu': {'value': 0, 'unit': 'bool'}, 'RL Pumpe': {'value': 1, 'unit': 'bool'}, 'BPA': {'value': 0, 'unit': 'bool'}, 'BP1': {'value': 0, 'unit': 'bool'}, 'BP2': {'value': 0, 'unit': 'bool'}, 'BP3': {'value': 0, 'unit': 'bool'}, 'BZPA': {'value': 0, 'unit': 'bool'}, 'BZP1': {'value': 1, 'unit': 'bool'}, 'BZP2': {'value': 0, 'unit': 'bool'}, 'BZP3': {'value': 0, 'unit': 'bool'}, 'EHKP': {'value': 0, 'unit': 'bool'}, 'EHKP2': {'value': 0, 'unit': 'bool'}, 'EHKP3': {'value': 0, 'unit': 'bool'}, 'EHK Anf': {'value': 0, 'unit': 'bool'}, 'EHK Anf2': {'value': 0, 'unit': 'bool'}, 'EHK Anf3': {'value': 0, 'unit': 'bool'}, 'HKP3': {'value': 0, 'unit': 'bool'}, 'M3A': {'value': 0, 'unit': 'bool'}, 'M3Z': {'value': 0, 'unit': 'bool'}, 'HKP4': {'value': 0, 'unit': 'bool'}, 'M4A': {'value': 0, 'unit': 'bool'}, 'M4Z': {'value': 0, 'unit': 'bool'}, 'HKP5': {'value': 0, 'unit': 'bool'}, 'M5A': {'value': 0, 'unit': 'bool'}, 'M5Z': {'value': 0, 'unit': 'bool'}, 'HKP6': {'value': 0, 'unit': 'bool'}, 'M6A': {'value': 0, 'unit': 'bool'}, 'M6Z': {'value': 0, 'unit': 'bool'}, 'PuffP': {'value': 0, 'unit': 'bool'}, 'Entasch gesp.': {'value': 0, 'unit': 'bool'}, 'ATW': {'value': 0, 'unit': 'bool'}, 'KASK1 Run': {'value': 0, 'unit': 'bool'}, 'KASK2 Run': {'value': 0, 'unit': 'bool'}, 'KASK3 Run': {'value': 0, 'unit': 'bool'}, 'KASK4 Run': {'value': 0, 'unit': 'bool'}, 'FW Freig.': {'value': 0, 'unit': 'bool'}, 'sAS Anf Füll': {'value': 0, 'unit': 'bool'}, 'HKV': {'value': 0, 'unit': 'bool'}, 'FLP': {'value': 0, 'unit': 'bool'}, 'Netztrafo': {'value': 1, 'unit': 'bool'}, 'Netzrelais': {'value': 1, 'unit': 'bool'}, 'Lagerraum': {'value': 0, 'unit': 'bool'}, 'Aschebox': {'value': 1, 'unit': 'bool'}, 'gFlP': {'value': 0, 'unit': 'bool'}, 'gFlM auf': {'value': 0, 'unit': 'bool'}, 'gFlM zu': {'value': 0, 'unit': 'bool'}, 'Spülung Aktiv': {'value': 0, 'unit': 'bool'}, 'DReg P1': {'value': 0, 'unit': 'bool'}, 'DReg P2': {'value': 0, 'unit': 'bool'}, 'DReg Mi auf': {'value': 0, 'unit': 'bool'}, 'DReg Mi zu': {'value': 0, 'unit': 'bool'}, 'Oel Out': {'value': 0, 'unit': 'bool'}, 'DReg2 P1': {'value': 0, 'unit': 'bool'}, 'DReg2 P2': {'value': 0, 'unit': 'bool'}, 'DReg2 Mi auf': {'value': 0, 'unit': 'bool'}, 'DReg2 Mi zu': {'value': 0, 'unit': 'bool'}}
result = hargassner.parse_line(test_line1, full_channel_infos)
if result == expected_result:
    print("Passed.")
else:
    print("Failed! Parsed data:")
    print(result)
    print("Should be:")
    print(expected_result)
print("\n")


print("Testing parse_line(test_line1, partial_channel_infos)")
expected_result = {'ZK': {'value': '8', 'unit': ''}, 'O2': {'value': '1.2', 'unit': '%'}, 'O2soll': {'value': '8.4', 'unit': '%'}, 'TK': {'value': '58', 'unit': '°C'}, 'TKsoll': {'value': '48', 'unit': '°C'}, 'TRG': {'value': '60', 'unit': '°C'}, 'SZist': {'value': '9', 'unit': '%'}, 'FWS3 D': {'value': '0', 'unit': 'l/min'}, 'FWS4 Anf.': {'value': '0', 'unit': '°C'}, 'FWS4 Pumpe': {'value': '0', 'unit': '%'}, 'FWS4 Leist': {'value': '0', 'unit': 'kW'}, 'FWS4 T': {'value': '0', 'unit': '°C'}, 'FWS4 D': {'value': '0', 'unit': 'l/min'}, 'DiffReg2 S3': {'value': '-20', 'unit': '°C'}, 'DiffReg2 S4': {'value': '-20', 'unit': '°C'}, 'Stb': {'value': 1, 'unit': 'bool'}, 'Fuellstand': {'value': 1, 'unit': 'bool'}, 'Es Rein Endl': {'value': 0, 'unit': 'bool'}, 'HKPA': {'value': 0, 'unit': 'bool'}, 'MAA': {'value': 0, 'unit': 'bool'}, 'MAZ': {'value': 0, 'unit': 'bool'}, 'HKP1': {'value': 1, 'unit': 'bool'}, 'M1A': {'value': 0, 'unit': 'bool'}, 'gFlP': {'value': 0, 'unit': 'bool'}, 'gFlM auf': {'value': 0, 'unit': 'bool'}, 'gFlM zu': {'value': 0, 'unit': 'bool'}, 'Spülung Aktiv': {'value': 0, 'unit': 'bool'}, 'DReg P1': {'value': 0, 'unit': 'bool'}, 'DReg P2': {'value': 0, 'unit': 'bool'}, 'DReg Mi auf': {'value': 0, 'unit': 'bool'}, 'DReg Mi zu': {'value': 0, 'unit': 'bool'}, 'Oel Out': {'value': 0, 'unit': 'bool'}, 'DReg2 P1': {'value': 0, 'unit': 'bool'}, 'DReg2 P2': {'value': 0, 'unit': 'bool'}, 'DReg2 Mi auf': {'value': 0, 'unit': 'bool'}, 'DReg2 Mi zu': {'value': 0, 'unit': 'bool'}}
result = hargassner.parse_line(test_line1, partial_channel_infos)
if result == expected_result:
    print("Passed.")
else:
    print("Failed! Parsed data:")
    print(result)
    print("Should be:")
    print(expected_result)
print("\n")


print("Testing compare_parsed_data(test_line1, test_data2)")
test_data1 = hargassner.parse_line(test_line1, full_channel_infos)
test_data2 = hargassner.parse_line(test_line2, full_channel_infos)
expected_result = {'TPm': {'value': '110', 'unit': '°C'}, 'UsePos': {'value': '0', 'unit': ''}, 'Aschebox': {'value': 0, 'unit': 'bool'}}
result = hargassner.compare_parsed_data(test_data1, test_data2)
if result == expected_result:
    print("Passed.")
else:
    print("Failed! Parsed data:")
    print(result)
    print("Should be:")
    print(expected_result)
print("\n")


print("Testing compare_parsed_data(test_data1, test_data3)")
test_data3 = test_data1.copy()
del test_data3['O2soll']
expected_result = {'O2soll': {'value': '8.4', 'unit': '%'}, 'TPm': {'value': '110', 'unit': '°C'}, 'UsePos': {'value': '0', 'unit': ''}, 'Aschebox': {'value': 0, 'unit': 'bool'}}
result = hargassner.compare_parsed_data(test_data3, test_data2)
if result == expected_result:
    print("Passed.")
else:
    print("Failed! Parsed data:")
    print(result)
    print("Should be:")
    print(expected_result)
print("\n")


print("Testing parse_line(test_line1, partial_channel_infos)")
result = hargassner.import_config_file("config.json")
print(result)


#print("Testing parse_file('test\\telnet_data\\putty.log', channel_infos)")
#parse_file('test\\telnet_data\\putty.log', full_channel_infos)


#connect_and_parse('10.0.0.25', full_channel_infos)
