from api_keys import fbi_api_key
import requests
import pprint as pp
import time

fbi_api_key = fbi_api_key()

#def fbi_offender_national_api_call(offense_type,demographic_type):

offense_type = 'prostitution-offenses'
demographic_type = 'sex'

full_url = 'https://api.usa.gov/crime/fbi/sapi/api/data/nibrs/' + offense_type + '/offender/national/' + demographic_type + '?API_KEY=' + fbi_api_key
request = requests.get(full_url)


if request.status_code == 200:
    request = request.json()
    results = request['results']

    #If Results List is Not Empty
    if not results:
        print('list is empty')

    else:
        #Space Results
        number_of_results = len(results)
        male_count = [None]*number_of_results
        female_count = [None]*number_of_results
        unknown = [None]*number_of_results
        data_year = [None]*number_of_results
        result_index = 0

        #For Each Result in Results
        for result in results:
            male_count[result_index] = result['male_count']
            female_count[result_index] = result['female_count']
            unknown[result_index] = result['unknown']
            data_year[result_index] = result['data_year']
            result_index += 1

        time.sleep(10)
        return [male_count,female_count,unknown,data_year]

while request.status_code == 429:
    print('too many requests! Waiting...')
    time.sleep(10)

    request = requests.get(full_url)

    if request.status_code == 200:
        request = request.json()
        results = request['results']

        #If Results List is Not Empty
        if not results:
            print('list is empty')

        else:
            #Space Results
            number_of_results = len(results)
            male_count = [None]*number_of_results
            female_count = [None]*number_of_results
            unknown = [None]*number_of_results
            data_year = [None]*number_of_results
            result_index = 0

            #For Each Result in Results
            for result in results:
                male_count[result_index] = result['male_count']
                female_count[result_index] = result['female_count']
                unknown[result_index] = result['unknown']
                data_year[result_index] = result['data_year']
                result_index += 1

            time.sleep(10)
            return [male_count,female_count,unknown,data_year]