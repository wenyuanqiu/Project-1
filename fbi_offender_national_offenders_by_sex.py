import requests
import pprint as pp
import pandas as pd
from fbi_offender_national_api_call_by_sex import fbi_offender_national_api_call_by_sex
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

male_count = []
female_count = []
unknown = []
data_year = []
offense_type_list = []

request_number = 0

for offense_type in offense_types_list:
    demographic_types = 'sex'
    print(f'offense type: {offense_type}, request number: {request_number}')
    results = fbi_offender_national_api_call_by_sex(offense_type,demographic_types)
    try:
        male_count.extend(results[0])
        female_count.extend(results[1])
        unknown.extend(results[2])
        data_year.extend(results[3])
        offense_type_list.extend(results[4])
        request_number += 1
    except:
        request_number += 1

pickle_path = r'data\rawdata\offenders_by_sex\male_count.pkl'
pickle.dump(male_count, open(pickle_path, "wb" ))

pickle_path = r'data\rawdata\offenders_by_sex\female_count.pkl'
pickle.dump(female_count, open(pickle_path, "wb" ))

pickle_path = r'data\rawdata\offenders_by_sex\unknown.pkl'
pickle.dump(unknown, open(pickle_path, "wb" ))

pickle_path = r'data\rawdata\offenders_by_sex\data_year.pkl'
pickle.dump(data_year, open(pickle_path, "wb" ))

pickle_path = r'data\rawdata\offenders_by_sex\offense_type_list.pkl'
pickle.dump(offense_type_list, open(pickle_path, "wb" ))