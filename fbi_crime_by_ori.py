import requests
import pprint as pp
import pandas as pd
from fbi_crime_by_ori_api_call import fbi_crime_by_ori_api_call
import pickle
import time

csv_path = r'data\rawdata\All_States_ORIs.csv'
ori_data = pd.read_csv(csv_path)

oris_list = ori_data['ori'].unique().tolist()
start_year = 1990
end_year = 2017

oris = []
data_years = []
offenses = []
state_abbrs = []
cleareds = []
actuals = []
request_number = 0
request_number_last_milestone = 0

for ori in oris_list:

    print(ori,request_number)
    #if request_number - request_number_last_milestone > 400:
    #    time.sleep(4000)
    #    print('Waiting for 1 Hour')
    #    request_number_last_milestone = request_number

    results = fbi_crime_by_ori_api_call(ori,start_year,end_year)
    
    #Write to Lists
    try:
        oris.extend(results[0])
        data_years.extend(results[1])
        offenses.extend(results[2])
        state_abbrs.extend(results[3])
        cleareds.extend(results[4])
        actuals.extend(results[5])
        request_number += 1
    except:
        request_number += 1

pickle_path = r'data\rawdata\oris.pkl'
pickle.dump(oris, open(pickle_path, "wb" ))

pickle_path = r'data\rawdata\data_years.pkl'
pickle.dump(data_years, open(pickle_path, "wb" ))

pickle_path = r'data\rawdata\offenses.pkl'
pickle.dump(offenses, open(pickle_path, "wb" ))

pickle_path = r'data\rawdata\state_abbrs.pkl'
pickle.dump(state_abbrs, open(pickle_path, "wb" ))

pickle_path = r'data\rawdata\cleareds.pkl'
pickle.dump(cleareds, open(pickle_path, "wb" ))

pickle_path = r'data\rawdata\actuals.pkl'
pickle.dump(actuals, open(pickle_path, "wb" ))
    
    