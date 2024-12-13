# Final Project for CIS3120 - Fall 2024

## Author:
Erick Tecuatl

## Purpose of script:
To download stock data for a ticker and plot it on candlestick chart.
Users are able to input ticker and dates, as well as a choice of RSI(relative strength index) or EMA (exponential moving average) for the ticker. 
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


- Program has checks to ensure validity of data.  User will be prompted if ticker does not exist, dates are out of bounds, or improper date format.
API_Connection will check for any null values, although extremely unlikely, but added just in case.  

- Connection class masks API key in link and assigns it as a private value, given that link is ends with key=''.

- RSI is limited to a period of 14 as this is the most widly used period.  EMA is customizable but restricted to anything greater than 5 and less than 200, as extremes will skew and yield improper results.  Recommeneded EMA are 12,26,100,200.

**IMPORTANT NOTE:**  Due to plot limitations, an error will occur if rows retreieved are greater than 300 rows, but visualation will still plot. User will be able to zoom in and out of chart. 

## Links:
**pandas_ta RSI documentation:** (https://github.com/twopirllc/pandas-ta/blob/main/pandas_ta/momentum/rsi.py)

**mplfinance plotting documentation:** (https://github.com/matplotlib/mplfinance/blob/master/examples/addplot.ipynb)

**polygon.io API documentation:88 (https://polygon.io/docs/stocks?gad_source=1&gclid=Cj0KCQiAsOq6BhDuARIsAGQ4-zgdyGHHYAzBPQb40HaG_fqYcH8fMdxHZJ4p-9Q1rwHgzJsV8ZkbWDUaAgWrEALw_wcB#getting-started?utm_term=stock%20rest%20api&utm_campaign=Stocks+-+USA&utm_source=adwords&utm_medium=ppc&hsa_acc=4299129556&hsa_cam=1330311037&hsa_grp=133850757806&hsa_ad=591207294400&hsa_src=g&hsa_tgt=aud-896761709510:kwd-833268776823&hsa_kw=stock%20rest%20api&hsa_mt=p&hsa_net=adwords&hsa_ver=3/getting-started)

### polygon.io KEY REQUIRED BEFORE USE 
Key must be stored in .py file named erick_API_key.  If you desire to change file name, remember to change import in API_connection.py  
Format for key is: 

key = 'replace_text_with_key'
