import requests
import pprint as pp

endpoint = 'api/agencies'
web_url = f'https://api.usa.gov/crime/fbi/sapi/{endpoint}?api_key='
api_key = 'y8VHKmHAVqKKveJ5hFMkk9auO2jEyB4RaNOQSOgt'

full_url = web_url + api_key
full_url = 'https://api.usa.gov/crime/fbi/sapi/api/agencies?api_key=iiHnOKfno2Mgkt5AynpvPpUQTEyxE77jo1RU8PIv'

test = requests.get(full_url)
test = test.json()
pp.pprint(test)

