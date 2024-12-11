import pandas as pd
from API_connection import API_connection
import erick_API_key
from datetime import datetime

def exit_or_restart(input):
        """Handles Exit or Restart logic."""
        if input == 'EXIT':
            print("Exiting....")
            exit()
        elif input == 'RESTART':
            print("RESTARTING.....")
            main()
        else:
            return

def valid_date_check(date):
    """Double checks if the date is in the correct format."""
    while True:
        date_input = input(f"Enter a {date} date in this format 'YYYY-MM-DD': ").upper()
        if date_input in ['EXIT','RESTART']:
            exit_or_restart(date_input)
        try:
            valid_date = datetime.strptime(date_input, '%Y-%m-%d')
            return valid_date.strftime('%Y-%m-%d')  
        except ValueError:
            print("Invalid date format. Please enter date in this format: 'YYYY-MM-DD'.")
        

#First Ticker Set Up
def ticker1_input():
    while True: 
        ticker1 = input("Enter the first ticker: ").upper()
        if ticker1 in ['EXIT', 'RESTART']:
            exit_or_restart(ticker1)

        #Calls the valid_date_check function to check if format is correct. 
        start_date1 = valid_date_check('start')
        end_date1 = valid_date_check('end')
        
        #Initialize Dataframe 
        api = API_connection()
        df1 = api.ticker1_connection(ticker1,start_date1,end_date1)
        #Checking if Data is missing/ticker doesn't exist
        if df1.empty:
             print(f"No Data found for {ticker1}. Please double check date format or Ticker Name. ")
        else:
             print(f"Data for {ticker1} found.")
             return ticker1,df1
        
#Second Ticker Set up         
def ticker2_input():
    #User input and options.  User can exit at anytime. 
    while True: 
        ticker2 = input("Enter the second ticker: ").upper()
        if ticker2 in ['EXIT', 'RESTART']:
            exit_or_restart(ticker2)

        #Calls the valid_date_check function to check if format is correct. 
        start_date2 = valid_date_check('start')
        end_date2 = valid_date_check('end')
        
        #calling API_connection class
        api = API_connection()
        df2 = api.ticker2_connection(ticker2,start_date2,end_date2)
        #Checking if Data is missing/ticker doesn't exist
        if df2.empty:
             print(f"Invalid Data for {ticker2}. Please double check date format or Ticker Name.")
        else:
             print(f"Data for {ticker2} found.")
             return ticker2,df2

def main():
    #Notifying user option to restart or exit at any time. 
    print("IMPORTANT: TYPE 'EXIT' TO EXIT AT ANYTIME.  TYPE 'RESTART' AT ANYTIME TO BEGIN AT FIRST TICKER.")
    #initializing First ticker:
    ticker1,df1 =  ticker1_input()  

    #initializing Second Ticker:
    ticker2,df2 = ticker2_input()

    #main menu
    print("IMPORTANT: TYPE 'EXIT' TO EXIT AT ANYTIME.  TYPE 'RESTART' AT ANYTIME TO BEGIN AT FIRST TICKER.")
    user_input = input(f"MAIN MENU \nPlease select your option from a list.\n"
                        f"1. Plot {ticker1} on a chart.\n"
                        f"2. Plot {ticker2} on a chart.\n"
                        f"3. Plot both tickers on one chart.\n"
                        f"4. Add EMA on {ticker1}.\n"
                        f"5. Add EMA on {ticker2}\n"
                        f"6. Select new tickers.\n").upper()
    #Error Handling options.
    exit_or_restart(user_input)

main()
