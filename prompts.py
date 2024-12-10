import pandas as pd
from API_connection import API_connection
import erick_API_key

def ticker1_df(ticker1,start_date1,end_date1):
    #retrieve dataframe from API_Connection
    api = API_connection()
    df1 = api.ticker1_connection(ticker1,start_date1,end_date1)
    #print(f"Dataframe for {ticker1} :\n {df1}")
    print(f"Dataframe returned for {ticker1}")
    return(df1)

def ticker2_df(ticker2,start_date2,end_date2):
    #retrieve dataframe from API_Connection
    api = API_connection()
    df2 = api.ticker1_connection(ticker2,start_date2,end_date2)
    #print(f"Dataframe for {ticker2} :\n {df2}")
    print(f"Dataframe returned for {ticker2}")
    return(df2)


def main():
    #ticker 1 Set Up
    ticker1 = input("Enter the first ticker: ").upper()
    start_date1 = input("Enter a start date in this format 'YYYY-MM-DD': ")
    end_date1 = input("Enter an end date in this format 'YYYY-MM-DD':  ")
    ticker1_df(ticker1,start_date1,end_date1)
    #ticket 2 Set Up
    ticker2 = input("Enter the second ticker: ").upper()
    start_date2 = input("Enter a start date in this format 'YYYY-MM-DD': ")
    end_date2 = input("Enter an end date in this format 'YYYY-MM-DD':  ")
    ticker2_df(ticker2,start_date2,end_date2)
    # print(f"Here is your first ticker: {ticker1}")
    # print(f"Here is your second ticker: {ticker2}")
    # input(f"Please select your option from a List:\n1. Plot {ticker1} on a chart. \n2. Plot {ticker2} on a chart.\n3. Plot both tickers on one chart. \n4. Add EMA on {ticker1}.\n5. Add EMA on {ticker2}\n6. Start over. ")

main()
