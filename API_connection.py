import erick_API_key
import requests
import pandas as pd

class API_Connection:
    '''This is setting up the connection to Polygon.io'''
    def __init__(self):
        #api key is stored in the file erick_API_key with contents being key = ''
        self.key = erick_API_key.key

    def _hide_key(self,url):
        '''Hides key in the URL'''
        return url.replace(self.key,"******")
    
    def api_key(self):
        '''Accessing key'''
        return self.key

class Ticker_Connection(API_Connection):
    '''Uses Key to build url and call API'''
    def ticker_connection(self,ticker,start_date,end_date):
        #sends these parameters to the url_parts to construct entire url.
        url = self._url_parts(ticker,start_date,end_date)
        hidden_url = self._hide_key(url)
        print(f"Hidden Url: {hidden_url}")
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame()
        #response code handling.
        if response.status_code == 200:
            print(f"Received API Response.  Code {response.status_code}")
            data_ticker = response.json()
            #checks to see if the object type is readable
            if isinstance(data_ticker,dict) and 'results' in data:
                results = data['results']
                if results:
                    #inserts and cleans data.
                    df = pd.DataFrame(results)
                    df.rename(columns={'t': 'Date', 'o': 'Open', 'h': 'High', 'l': 'Low', 'c': 'Close', 'v': 'Volume'}, inplace=True)
                    df['Date']= pd.to_datetime(df['Date'], unit='ms')#formatting into a date. 
                    df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
                    df['Date'] = pd.to_datetime(df['Date']) 
                    df.set_index('Date', inplace=True)
                    if df.isnull().any().any():  # Checks if there are any null values in the DataFrame.   There shouldn't be any null values in polygon but JUST in case. 
                        print("There are null values in the DataFrame.")
                        print("Dropping null values")
                        df.dropna(inplace=True)
                    else:
                        print("No null values in the DataFrame.")
                    #print(df.head())
                else:
                    print("No Results Found.")
            else:
                print("Wrong Format.")
        else:
            print(f"Invalid Response. Code: {response.status_code}")
        return df
    
    def _url_parts(self,ticker,start_date,end_date):
        '''Takes parameters and fills in variables in the API URL.'''
        return(f'https://api.polygon.io/v2/aggs/ticker/{ticker.upper()}/range/1/day/{start_date}/{end_date}?adjusted=true&sort=asc&apiKey={self.api_key()}')
    