from API_connection import Ticker_Connection
from datetime import datetime
import pandas as pd
import mplfinance as mpf
import pandas_ta as ta


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
    """User inputs information for First Ticker."""
    while True: 
        ticker1 = input("Enter the first ticker: ").upper()
        if ticker1 in ['EXIT', 'RESTART']:
            exit_or_restart(ticker1)

        #Calls the valid_date_check function to check if format is correct. 
        start_date = valid_date_check('start')
        end_date = valid_date_check('end')

        #Initialize Dataframe 
        api = Ticker_Connection()
        df1 = api.ticker_connection(ticker1,start_date,end_date)
        #Checking if Data is missing/ticker doesn't exist
        if df1.empty:
             print(f"No Data found for {ticker1}. Please double check date format or Ticker Name. ")
        else:
             print(f"Data for {ticker1} found.")
             return ticker1,df1
        
#Second Ticker Set up         
def ticker2_input():
    """User inputs information for Second Ticker."""
    while True: 
        ticker2 = input("Enter the second ticker: ").upper()
        if ticker2 in ['EXIT', 'RESTART']:
            exit_or_restart(ticker2)

        #Calls the valid_date_check function to check if format is correct. 
        start_date = valid_date_check('start')
        end_date = valid_date_check('end')
        
        #calling API_connection class
        api = Ticker_Connection()
        df2 = api.ticker_connection(ticker2,start_date,end_date)
        #Checking if Data is missing/ticker doesn't exist
        if df2.empty:
             print(f"Invalid Data for {ticker2}. Please double check date format or Ticker Name.")
        else:
             print(f"Data for {ticker2} found.")
             return ticker2,df2

def add_rsi(ticker,df,user_input):
    """Creating the RSI Indicator"""
    print(f"Adding RSI to {ticker}")
    df['RSI'] = ta.rsi(df['Close'], length=14)#imports the pandas_ta library
    rsi_plot = mpf.make_addplot(df['RSI'], panel=1, color='purple', width=1, ylabel='RSI')
    overbought = mpf.make_addplot([70] * len(df), panel=1, color='red', width=1, linestyle='--')
    oversold = mpf.make_addplot([30] * len(df), panel=1, color='green', width=1, linestyle='--')
    if user_input in ['3','5']:
        mpf.plot(df, type='candle', style='charles', title=f'Candlestick Chart for {ticker.upper()} with period=14 RSI', ylabel='Price', volume=True, addplot=[rsi_plot, overbought, oversold], panel_ratios=(3, 1))
        return
    return 


def add_ema(ticker,df,user_input):
    """Adds user input EMA"""
    print(f"Adding EMA to {ticker}")
    while True:
            try:
                ema_period=int(input("Enter desired EMA period between 5-200: "))
                if ema_period < 5 or ema_period > 200:
                    print("EMA out of bounds")
                else:
                    df['EMA'] = df['Close'].ewm(span=ema_period, adjust=False).mean()
                    ema = mpf.make_addplot(df['EMA'], color='blue', width=1)
                    #plotting EMA
                    if user_input in ['4','6']:
                        mpf.plot(df, type='candle', style='charles', title=f'Candlestick Chart for {ticker.upper()} with {ema_period} EMA',ylabel='Price', volume=True, addplot=ema) 
                        break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    return df,ema_period 

def main():
    """Main Menu and prompts user to select an option after ticker info."""
    #Notifying user option to restart or exit at any time. 
    print("IMPORTANT: TYPE 'EXIT' TO EXIT AT ANYTIME.  TYPE 'RESTART' AT ANYTIME TO BEGIN AT FIRST TICKER.")
    #initializing First ticker:
    ticker1,df1 =  ticker1_input()  

    #initializing Second Ticker:
    ticker2,df2 = ticker2_input()

    #printing results- serves as a check
    print(f"Ticker1-{ticker1}\n"
          f"{ticker1} Shape: {df1.shape}\n"
          f"{df1.head(3)}")
    print(f"Ticker2-{ticker2}\n"
          f"{ticker2} Shape: {df2.shape}\n"
          f"{df2.head(3)}")

    #main menu loop
    while True:
        print("IMPORTANT: TYPE 'EXIT' TO EXIT AT ANYTIME.  TYPE 'RESTART' AT ANYTIME TO BEGIN AT FIRST TICKER.")
        user_input = input(f"MAIN MENU \nPlease select your option from this list.\n"
                            f"1. Plot {ticker1} on a chart.\n"
                            f"2. Plot {ticker2} on a chart.\n"
                            f"3. Add RSI to {ticker1}.\n"
                            f"4. Add EMA on {ticker1}.\n"
                            f"5. Add RSI on {ticker2}.\n"
                            f"6. Add EMA on {ticker2}.\n").upper()
        
        #Main menu selection process.
        if user_input in ['EXIT', 'RESTART']:
            exit_or_restart(user_input)
        elif user_input == '1':
            print(f"Plotting Candlestick chart for {ticker1}")
            mpf.plot(df1, type='candle',style='charles',title=f'Candlestick Chart for {ticker1.upper()}',ylabel='Price',volume=True)
        elif user_input == '2':
            print(f"Plotting Candlestick chart for {ticker2}")
            mpf.plot(df2, type='candle',style='charles',title=f'Candlestick Chart for {ticker2.upper()}',ylabel='Price',volume=True)
        elif user_input =='3':#RSI
            add_rsi(ticker1,df1,user_input)
        elif user_input =='4':#EMA
            add_ema(ticker1,df1,user_input)
        elif user_input =='5':#RSI
            add_rsi(ticker2,df2,user_input)
        elif user_input == '6':#EMA
            add_ema(ticker2,df2,user_input)
        else: 
            print("Invalid option.  Please select an option from the list.")
        

main()