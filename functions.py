import requests
import json
import config

def get_countries () :

    request = requests.get(f'https://free.currconv.com/api/v7/currencies?apiKey={config.api_key}')

    with open('currencies.json', 'w') as f:
        json.dump(request.json(), f)

    with open('currencies.json', 'r') as f:
        json_data = json.load(f)


    for data in json_data['results']:
        print('')
        print('Currency Name: {}'.format(json_data['results'][data]['currencyName']))
        print('Currency Symbol: {}'.format(json_data['results'][data]['id']))
        print('')   
        
def convert_currency (currencyFrom, currencyTo, number) :
    request = requests.get(f'https://free.currconv.com/api/v7/convert?q={currencyFrom}_{currencyTo}&compact=ultra&apiKey={config.api_key}')

    result = request.json()[f'{currencyFrom}_{currencyTo}'] * number

    return result

