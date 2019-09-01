from api_keys import fbi_api_key
import requests
import pprint as pp
import time

fbi_api_key = fbi_api_key()

def fbi_crime_by_ori_api_call(ori,start_year,end_year):
    
    full_url = 'https://api.usa.gov/crime/fbi/sapi/api/summarized/agencies/' + ori + '/offenses/' + str(start_year) + '/' + str(end_year) + '?API_KEY=' + fbi_api_key
    request = requests.get(full_url)

    if request.status_code == 200:
        request = request.json()

        if type(request) is dict:
            results = request['results']
            print('request OK')
            number_of_results = len(results)
            oris = [None]*number_of_results
            data_years = [None]*number_of_results
            offenses = [None]*number_of_results
            state_abbrs = [None]*number_of_results
            cleareds = [None]*number_of_results
            actuals = [None]*number_of_results
            result_index = 0
            

            for result in results:
                oris[result_index] = result['ori']
                data_years[result_index] = result['data_year']
                offenses[result_index] = result['offense']
                state_abbrs[result_index] = result['state_abbr']
                cleareds[result_index] = result['cleared']
                actuals[result_index] = result['actual']
                result_index += 1
            
            time.sleep(10)    
            return [oris,data_years,offenses,state_abbrs,cleareds,actuals]
    
    while request.status_code == 429:
        print('too many requests! Waiting...')
        time.sleep(10)
        request = requests.get(full_url)

        if request.status_code == 200:
            request = request.json()

            if type(request) is dict:
                results = request['results']
                print('request OK')
                number_of_results = len(results)
                oris = [None]*number_of_results
                data_years = [None]*number_of_results
                offenses = [None]*number_of_results
                state_abbrs = [None]*number_of_results
                cleareds = [None]*number_of_results
                actuals = [None]*number_of_results
                result_index = 0

                for result in results:
                    oris[result_index] = result['ori']
                    data_years[result_index] = result['data_year']
                    offenses[result_index] = result['offense']
                    state_abbrs[result_index] = result['state_abbr']
                    cleareds[result_index] = result['cleared']
                    actuals[result_index] = result['actual']
                    result_index += 1
                
                time.sleep(10)
                return [oris,data_years,offenses,state_abbrs,cleareds,actuals]