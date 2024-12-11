import erick_API_key
import requests
import pandas as pd

class API_connection:
    '''This is setting up the connection to Polygon.io'''
    def __init__(self):
        #api key is stored in the file erick_API_key with contents being key = ''
        self.key = erick_API_key.key
    
    def ticker1_connection(self,ticker1,start_date1,end_date1):
        url1 = f'https://api.polygon.io/v2/aggs/ticker/{ticker1}/range/1/day/{start_date1}/{end_date1}?adjusted=true&sort=asc&apiKey={self.key}'
        print(f'Fetching response from url.')
        response = requests.get(url1)
        data = response.json()
        print(f'Response: {data}')
        if response.status_code == 200:
            data_ticker1 = response.json()
            #error handling
            if isinstance(data_ticker1,dict) and 'results' in data:
                results = data['results']
                if results:
                    df1 = pd.DataFrame(results)
                    print("Data Found")
            else:
                print("Invalid Ticker.")
                df1 = pd.DataFrame()
        else:
            print('Failed to fetch data from the API, or invalid Ticker.  Try again.')
            df1 = pd.DataFrame()
        return df1
    
    def ticker2_connection(self,ticker2,start_date2,end_date2):
        url2 = f'https://api.polygon.io/v2/aggs/ticker/{ticker2}/range/1/day/{start_date2}/{end_date2}?adjusted=true&sort=asc&apiKey={self.key}'
        print(f'Fetching response from url.')
        response = requests.get(url2)
        data2 = response.json()
        print(f'Response: {data2}')
        if response.status_code == 200:
            data_ticker2 = response.json()
            #error handling
            if isinstance(data_ticker2,dict) and 'results' in data2:
                results = data2['results']
                if results:
                    df2 = pd.DataFrame(results)
            else:
                print("Invalid Ticker.")
                df2 = pd.DataFrame()
        else:
            print('Failed to fetch data from the API, or invalid Ticker.  Try again.')
            df2 = pd.DataFrame()
        return df2