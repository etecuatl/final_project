import erick_API_key
import requests
import pandas as pd

class API_connection:
    '''This is setting up the connection to Polygon.io'''
    def __init__(self,API_key):
        self.API_key = API_key
        return API_key
    
    def ticker1_connection(ticker1,start_date,end_date,key):
        url1 = f'https://api.polygon.io/v2/aggs/ticker/{ticker1}/range/1/day/{start_date}/{end_date}?adjusted=true&sort=asc&apiKey={key}'
        print(f'Fetching response from url.')
        response = requests.get(url1)
        print(f'Response: {response}')
        if response.status_code == 200:
            data_ticker1 = response.json()
            df = pd.DataFrame.from_dict(data_ticker1)
        else:
            print('Failed to fetch data from the API')
        return data_ticker1
    
    def ticker2_connection(ticker2,start_date,end_date,key):
        url2 = f'https://api.polygon.io/v2/aggs/ticker/{ticker2}/range/1/day/{start_date}/{end_date}?adjusted=true&sort=asc&apiKey={key}'
        print(f'Fetching response from url.')
        response = requests.get(url2)
        print(f'Response: {response}')
        if response.status_code == 200:
            data_ticker2 = response.json()
            df = pd.DataFrame.from_dict(data_ticker2)
        else:
            print('Failed to fetch data from the API')
        return data_ticker2