import requests
import pprint as pp
import pandas as pd
from fbi_offender_national_api_call import fbi_offender_national_api_call
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

for offense_type in offense_types_list:
    for demographic_type in demographic_types_list:
        fbi_offender_national_api_call(offense_type,demographic_type)