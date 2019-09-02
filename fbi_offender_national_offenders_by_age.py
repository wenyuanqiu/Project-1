import requests
import pprint as pp
import pandas as pd
from fbi_offender_national_api_call_by_age import fbi_offender_national_api_call_by_sex
import pickle
import time

offense_types_list = ['aggravated-assault','all-other-larceny','all-other-offenses','animal-cruelty','arson','assisting-or-promoting-prostitution',
'bad-checks','betting','bribery','burglary-breaking-and-entering','counterfeiting-forgery','credit-card-automated-teller-machine-fraud',
'destruction-damage-vandalism-of-property','driving-under-the-influence','drug-equipment-violations','drug-violations','drunkenness','embezzlement',
'extortion-blackmail','false-pretenses-swindle-confidence-game','fondling','gambling-equipment-violation','hacking-computer-invasion',
'human-trafficking-commerical-sex-acts','human-trafficking-commerical-involuntary-servitude','identity-theft','impersonation','incest',
'intimidation','justifiable-homicide','kidnapping-abduction','motor-vehicle-theft','murder-and-nonnegligent-manslaughter','negligent-manslaughter',
'operating-promoting-assiting-gambling','curfew-loitering-vagrancy-violations','peeping-tom','pocket-picking','pornography-obscence-material',
'prostitution','purchasing-prostitution','purse-snatching','rape','robbery','sexual-assult-with-an-object','sex-offenses-non-forcible','shoplifting',
'simple-assault','sodomy','sports-tampering','statutory-rape','stolen-property-offenses','theft-from-building','theft-from-coin-operated-machine-or-device',
'theft-from-motor-vehicle','theft-of-motor-vehicle-parts-or-accessories','theft-from-motor-vehicle','weapon-law-violation','welfare-fraud','wire-fraud',
'not-specified','liquor-law-violations','crime-against-person','crime-against-property','crime-against-society','assault-offenses','homicide-offenses',
'human-trafficking-offenses','sex-offenses','sex-offenses-non-forcible',' fraud-offenses','larceny-theft-offenses',' drugs-narcotic-offenses',
'gambling-offenses','prostitution-offenses','all-offenses']
demographic_types_list = ['age','count','ethnicity','race','sex']

unknown = []
range_0_9 = []
range_10_19 = []
range_20_29 = []
range_30_39 = []
range_40_49 = []
range_50_59 = []
range_60_69 = []
range_70_79 = []
range_80_89 = []
range_90_99 = []
data_year = []
offense_type_list = []
request_number = 0

for offense_type in offense_types_list:
    demographic_types = 'age'
    print(f'offense type: {offense_type}, request number: {request_number}')
    results = fbi_offender_national_api_call_by_sex(offense_type,demographic_types)
    try:
        unknown.extend(results[0])
        range_0_9.extend(results[1])
        range_10_19.extend(results[2])
        range_20_29.extend(results[3])
        range_30_39.extend(results[4])
        range_40_49.extend(results[5])
        range_50_59.extend(results[6])
        range_60_69.extend(results[7])
        range_70_79.extend(results[8])
        range_80_89.extend(results[9])
        range_90_99.extend(results[10])
        data_year.extend(results[11])
        offense_type_list.extend(results[12])
        request_number += 1
    except:
        request_number += 1

pickle_path = r'data\rawdata\offenders_by_age\unknown.pkl'
pickle.dump(unknown, open(pickle_path, "wb" ))
pickle_path = r'data\rawdata\offenders_by_age\range_0_9.pkl'
pickle.dump(range_0_9, open(pickle_path, "wb" ))
pickle_path = r'data\rawdata\offenders_by_age\range_10_19.pkl'
pickle.dump(range_10_19, open(pickle_path, "wb" ))
pickle_path = r'data\rawdata\offenders_by_age\range_20_29.pkl'
pickle.dump(range_20_29, open(pickle_path, "wb" ))
pickle_path = r'data\rawdata\offenders_by_age\range_30_39.pkl'
pickle.dump(range_30_39, open(pickle_path, "wb" ))
pickle_path = r'data\rawdata\offenders_by_age\range_40_49.pkl'
pickle.dump(range_40_49, open(pickle_path, "wb" ))
pickle_path = r'data\rawdata\offenders_by_age\range_50_59.pkl'
pickle.dump(range_50_59, open(pickle_path, "wb" ))
pickle_path = r'data\rawdata\offenders_by_age\range_60_69.pkl'
pickle.dump(range_60_69, open(pickle_path, "wb" ))
pickle_path = r'data\rawdata\offenders_by_age\range_70_79.pkl'
pickle.dump(range_70_79, open(pickle_path, "wb" ))
pickle_path = r'data\rawdata\offenders_by_age\range_80_89.pkl'
pickle.dump(range_80_89, open(pickle_path, "wb" ))
pickle_path = r'data\rawdata\offenders_by_age\range_90_99.pkl'
pickle.dump(range_90_99, open(pickle_path, "wb" ))
pickle_path = r'data\rawdata\offenders_by_age\data_year.pkl'
pickle.dump(data_year, open(pickle_path, "wb" ))
pickle_path = r'data\rawdata\offenders_by_age\offense_type_list.pkl'
pickle.dump(offense_type_list, open(pickle_path, "wb" ))

