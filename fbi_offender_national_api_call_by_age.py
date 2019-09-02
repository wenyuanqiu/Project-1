from api_keys import fbi_api_key
import requests
import pprint as pp
import time

fbi_api_key = fbi_api_key()

#def fbi_offender_national_api_call(offense_type,demographic_type):

def fbi_offender_national_api_call_by_sex(offense_type, demographic_type):

    full_url = 'https://api.usa.gov/crime/fbi/sapi/api/data/nibrs/' + offense_type + '/offender/national/' + demographic_type + '?API_KEY=' + fbi_api_key
    request = requests.get(full_url)


    if request.status_code == 200:
        request = request.json()
        results = request['results']

        #If Results List is Not Empty
        if not results:
            print('results are empty')

        else:
            #Space Results
            number_of_results = len(results)
            unknown = [None]*number_of_results
            range_0_9 = [None]*number_of_results
            range_10_19 = [None]*number_of_results
            range_20_29 = [None]*number_of_results
            range_30_39 = [None]*number_of_results
            range_40_49 = [None]*number_of_results
            range_50_59 = [None]*number_of_results
            range_60_69 = [None]*number_of_results
            range_70_79 = [None]*number_of_results
            range_80_89 = [None]*number_of_results
            range_90_99 = [None]*number_of_results
            data_year = [None]*number_of_results
            offense_type_list = [None]*number_of_results
            result_index = 0

            #For Each Result in Results
            for result in results:
                unknown[result_index] = result['unknown']
                range_0_9[result_index] = result['range_0_9']
                range_10_19[result_index] = result['range_10_19']
                range_20_29[result_index] = result['range_20_29']
                range_30_39[result_index] = result['range_30_39']
                range_40_49[result_index] = result['range_40_49']
                range_50_59[result_index] = result['range_50_59']
                range_60_69[result_index] = result['range_60_69']
                range_70_79[result_index] = result['range_70_79']
                range_80_89[result_index] = result['range_80_89']
                range_90_99[result_index] = result['range_90_99']
                data_year[result_index] = result['data_year']
                offense_type_list[result_index] = offense_type
                result_index += 1

            #time.sleep(10)
            return [unknown,range_0_9,range_10_19,range_20_29,range_30_39,range_40_49,range_50_59,range_60_69,range_70_79,range_80_89,range_90_99,data_year,offense_type_list]