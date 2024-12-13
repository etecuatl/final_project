from API_connection import Ticker_Connection
from datetime import datetime
import pandas as pd
import mplfinance as mpf
import pandas_ta as ta


def exit_or_restart(input):
        """Handles Exit or Restart logic. Available at point for the user./"""
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
        date_input = input(f"Enter a {date} date in this format 'YYYY-MM-DD' after the year 2004: ").upper()
        if date_input in ['EXIT','RESTART']:
            exit_or_restart(date_input)
        try:
            valid_date = datetime.strptime(date_input, '%Y-%m-%d')
            return valid_date.strftime('%Y-%m-%d')  
        except ValueError:
            print("Invalid date format or year out of bounds. Please enter date in this format: 'YYYY-MM-DD'.")
        

#First Ticker Set Up
def ticker_input():
    """User inputs information for a Ticker."""
    while True: 
        ticker = input("Enter a ticker: ").upper()
        if ticker in ['EXIT', 'RESTART']:
            exit_or_restart(ticker)

        #Calls the valid_date_check function to check if format is correct. 
        start_date = valid_date_check('start')
        end_date = valid_date_check('end')

        #Initialize Dataframe by calling the API_Connection class.
        api = Ticker_Connection()
        df = api.ticker_connection(ticker,start_date,end_date)
        #Checking if Data is missing/ticker doesn't exist
        if df.empty:
             print(f"No Data found for {ticker}. Please double check date format or Ticker Name. ")
        else:
             print(f"Data for {ticker} found.")
             return ticker,df

def add_rsi(ticker,df,user_input):
    """Creating the RSI Indicator if user selects option 2."""
    print(f"Adding RSI to {ticker}")
    #creates indicator as another df using pandas_ta
    df['RSI'] = ta.rsi(df['Close'], length=14)#imports the pandas_ta library
    rsi_plot = mpf.make_addplot(df['RSI'], panel=1, color='purple', width=1, ylabel='RSI')
    #creating bounds for overbought or oversold signals. 
    overbought = mpf.make_addplot([70] * len(df), panel=1, color='red', width=1, linestyle='--')
    oversold = mpf.make_addplot([30] * len(df), panel=1, color='green', width=1, linestyle='--')
    if user_input in ['2']:
        mpf.plot(df, type='candle', style='charles', title=f'Candlestick Chart for {ticker.upper()} with period=14 RSI', ylabel='Price', volume=True, addplot=[rsi_plot, overbought, oversold], panel_ratios=(3, 1))
        return
    return 


def add_ema(ticker,df,user_input):
    """Adds user input EMA and plots if user selects option 3"""
    print(f"Adding EMA to {ticker}")
    counter = 0
    while True:
        try:
            if counter != '0':#adding counter for occasions where User is unable to set another RSI if desired to go back to another option
                ema_period=int(input("Enter desired EMA period between 5-200: "))
                counter += ema_period
            #adding restrictions to EMA as these are the most popular.  Anything less or more doesn't make sense.     
            if ema_period < 5 or ema_period > 200:
                print("EMA out of bounds")
            else:
                #creates a dataframe out of EMA and plots it if user selects option 3
                df['EMA'] = df['Close'].ewm(span=ema_period, adjust=False).mean()
                ema = mpf.make_addplot(df['EMA'], color='blue', width=1)
                #plotting EMA
                if user_input in ['3']:
                    mpf.plot(df, type='candle', style='charles', title=f'Candlestick Chart for {ticker.upper()} with {ema_period} EMA',ylabel='Price', volume=True, addplot=ema) 
                    break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return df,ema_period 

def main():
    """Main Menu and prompts user to select an option after ticker info."""
    #Notifying user option to restart or exit at any time. 
    print("IMPORTANT: TYPE 'EXIT' TO EXIT AT ANYTIME.  TYPE 'RESTART' AT ANYTIME TO SELECT A NEW TICKER.")
    #initializing ticker selection
    ticker,df =  ticker_input()  

    #printing results- serves as a check, prints first 3 rows.
    print(f"Ticker-{ticker}\n"
          f"{ticker} Shape: {df.shape}\n"
          f"{df.head(3)}")

    #main menu loop
    while True:
        print("IMPORTANT: TYPE 'EXIT' TO EXIT AT ANYTIME.  TYPE 'RESTART' AT ANYTIME TO SELECT A NEW TICKER.")
        user_input = input(f"MAIN MENU \nPlease select your option from this list.\n"
                            f"1. Plot {ticker} on a chart.\n"
                            f"2. Add RSI to {ticker}.\n"
                            f"3. Add EMA on {ticker}.\n").upper()
        
        #Main menu selection process.
        if user_input in ['EXIT', 'RESTART']:
            exit_or_restart(user_input)
        elif user_input == '1':
            print(f"Plotting Candlestick chart for {ticker}")
            mpf.plot(df, type='candle',style='charles',title=f'Candlestick Chart for {ticker.upper()}',ylabel='Price',volume=True)
        elif user_input == '2':#RSI
            add_rsi(ticker,df,user_input)
        elif user_input =='3':#EMA
            add_ema(ticker,df,user_input)
        else: 
            print("Invalid option.  Please select an option from the list.")
        

main()