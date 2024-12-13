# Final Project for CIS3120 - Fall 2024

## Author:
Erick Tecuatl

## Purpose of script:
To download stock data for a ticker and plot it on candlestick chart.
Users are able to input ticker and dates, as well as a choice of RSI or EMA for the ticker. 
Data is downloaded using the polygon.io API. 

## Prerequisites/Libraries Used:
    pip install pandas_ta
    pip intall mplfinance
    pandas
    datetime

## Highlights:
Program features a menu with options to select from.  User can type 'exit' or 'restart' to select tickers at any point.
![image](https://github.com/user-attachments/assets/f5d18ebc-4782-42cc-9257-d50f580bdae7)

Example of Chart with RSI Indicator:

<img src="https://github.com/user-attachments/assets/4b12220d-93ab-4e1c-8ec3-f10afb871cd0" width="50%" />


Program has checks to ensure validity of data.  User will be prompted if ticker does not exist, or dates are out of bounds.
API_Connection will check for any null values, although extremely unlikely, but added just in case.  

**IMPORTANT NOTE:** Given limitations of the API, only data from 2004-present day can be downloaded. API will return code 400 if year exceeds 2004.

## Links:
**pandas_ta RSI documentation:** (https://github.com/twopirllc/pandas-ta/blob/main/pandas_ta/momentum/rsi.py)

**mplfinance plotting documentation:** (https://github.com/matplotlib/mplfinance/blob/master/examples/addplot.ipynb)

### polygon.io KEY REQUIRED BEFORE USE 
