# -*- coding: utf-8 -*-
"""
Created on Mon May  8 13:06:52 2023

@author: Tomson
"""
import sys
import logging
from datetime import datetime as dt
import requests 
import pandas as pd
from pandas import json_normalize
import datetime
from utils.credentials import _ALPACA_ACCESS_KEY,_ALPACA_SECRET_KEY
from utils.credentials import _host, _port, _dbname, _user, _password
import time
import pymysql
import pytz
import schedule

def market_data(ticker,timeframe,days_before):
    yesterday = datetime.datetime.now() - datetime.timedelta(days=days_before)
    start = yesterday.replace(hour=0, minute=00, second=0, microsecond=0)
    start = start.isoformat()
    endpoint = 'https://data.alpaca.markets/v2/stocks/{}/bars?start={}Z&timeframe={}&limit=10000'#'#&after=true'
    formatted_endpoint = endpoint.format(ticker, start, timeframe)
    headers = {
            'accept': 'application/json',
            'APCA-API-KEY-ID':_ALPACA_ACCESS_KEY,
            'APCA-API-SECRET-KEY':_ALPACA_SECRET_KEY
        }
    
    response = requests.get(formatted_endpoint,
        headers=headers,
        timeout=5
    )
    
    # Response Handler
    status_OK = 200
    status_OK_message = 'OK | Market Data Updated'
    status_BadRequest = 400
    status_BadRequest_message = 'Bad Request | Invalid value for query parameter'
    status_Forbidden = 403
    status_Forbidden_message = 'Forbidden | Unauthorized'
    status_Unprocessable = 422
    status_Unprocessable_message = 'Unprocessable |​ Invalid query parameter'
    status_Requests = 429
    status_Requests_message = 'Too Many requests | ​Rate limit exceeded'
    
    #Response OK
    if response.status_code == status_OK:
        api_response = response.json()
    
        #Formatting response
        api_response_df = json_normalize(api_response['bars'])
        
        #Set index
        api_response_df.set_index('t', inplace=True)
        api_response_df.index.rename('Date', inplace=True)
        
        api_response_df.rename(
            columns={
                'o': 'Open',
                'h': 'High',
                'l': 'Low',
                'c': 'Close',
                'v': 'Volume',
                'n': 'Trades',
                'vw': 'VWAP',
            },
            inplace='True'
        )
        
        #Debug
        print(str(response.status_code)+' | '+status_OK_message)
        logging.info(str(dt.today())+' | ' +
                     str(response.status_code)+' | '+status_OK_message)
    
    #Error
    else:
    
        #Debug
        print(' === ERROR === ')
        if response.status_code == status_BadRequest:
            error_message = status_BadRequest_message
            print(str(response.status_code)+' | '+error_message)
    
        elif response.status_code == status_Forbidden:
            error_message = status_Forbidden_message
            print(str(response.status_code)+' | '+error_message)
    
        elif response.status_code == status_Unprocessable:
            error_message = status_Unprocessable_message
            print(str(response.status_code)+' | '+error_message)
    
        elif response.status_code == status_Requests:
            error_message = status_Requests_message
            print(str(response.status_code)+' | '+error_message)
    
        logging.error(str(dt.today())+' | ' +
                      str(response.status_code)+' | '+error_message)
        logging.shutdown()
        sys.exit('Market Data connection failed')
        return
    
    return api_response_df

def update_database(table_name, ticker):
    start_time = time.time()
    logging.info("Table selected: %s", table_name)
    conn = pymysql.connect(host=_host, user=_user, port=_port,
                           passwd=_password, db=_dbname, autocommit=True)
    c = conn.cursor()
    c.execute(
        "SELECT * FROM {} ORDER BY datetime DESC LIMIT {};".format(table_name, 50))
    existing_data = c.fetchall()
    existing_df = pd.DataFrame(existing_data, columns=[
                               'Datetime', 'Open', 'High', 'Low', 'Close', 'Volume', 'Trade Count', 'VWAP'])
    existing_df = ((existing_df.set_index("Datetime")
                    ).sort_index()).reset_index()
    existing_df['Datetime'] = pd.to_datetime(existing_df['Datetime'], utc=True)
    existing_df['Datetime'] = existing_df['Datetime'].dt.tz_convert(
        'America/New_York')

    if table_name in ("1T_SPY", "1T_QQQ"):
        timeframe = "1Min"
    elif table_name in ("5T_SPY", "5T_QQQ"):
        timeframe = "5Min"
    elif table_name in ("1H_SPY", "1H_QQQ"):
        timeframe = "1H"
    elif table_name in ("1D_SPY", "1D_QQQ"):
        timeframe = "1D"
    elif table_name in ("1W_SPY", "1W_QQQ"):
        timeframe = "1W"
    else:
        logging.error("Invalid table input")
        return

    if timeframe == "1Min":
        days_before = 3
    elif timeframe == "5Min":
        days_before = 6
    elif timeframe == "1H":
        days_before = 5
    elif timeframe == "1D":
        days_before = 5
    elif timeframe == "1W":
        days_before = 7
    else:
        logging.error("Invalid refresh interval input")
        return

    new_df = market_data(ticker, timeframe=timeframe, days_before=days_before)
    new_df = new_df.rename(columns={'Trades': 'Trade Count'})
    new_df.index = pd.to_datetime(new_df.index).rename("Datetime")
    timezone = pytz.timezone('America/New_York')
    new_df.index = new_df.index.tz_convert(timezone)

    if table_name in ("1T_SPY", "1T_QQQ"):
        fillhours = "1T"
        new_df = new_df.resample(fillhours).ffill()
    elif table_name in ("5T_SPY", "5T_QQQ"):
        fillhours = "5T"
        new_df = new_df.resample(fillhours).ffill()
    elif table_name in ("1H_SPY", "1H_QQQ"):
        fillhours = "1H"
        new_df = new_df.resample(fillhours).ffill()
    elif table_name in ("1D_SPY", "1D_QQQ"):
        fillhours = "1D"
        new_df = new_df.resample(fillhours).ffill()
    elif table_name in ("1W_SPY", "1W_QQQ"):
        new_df = new_df
    else:
        logging.error("Invalid table input")
        return

    new_df = new_df.reset_index()
    new_df['Datetime'] = new_df['Datetime'].dt.tz_convert('America/New_York')
    new_df = new_df.set_index("Datetime")
    startdate = pd.to_datetime(existing_df.iloc[-1]['Datetime'])
    iloc_start = new_df.index.get_loc(startdate)
    new_df = (new_df.iloc[iloc_start:])
    new_df = new_df.reset_index()
    if new_df.empty:
        logging.info("No new data")
    else:
        for _, row in new_df.iterrows():
            print(row[0], row[1], row[2], row[3], row[4])
            #logging.info("Added: %s", pd.DataFrame(row))
            timestamp = row['Datetime']
            open_val = row['Open']
            high_val = row['High']
            low_val = row['Low']
            close_val = row['Close']
            volume = row['Volume']
            trade_count = row['Trade Count']
            vwap = row['VWAP']

            c.execute("REPLACE INTO {} (Datetime, Open, High, Low, Close, Volume, `Trade Count`, VWAP) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)".format(table_name),
                      (timestamp, float(open_val), float(high_val), float(low_val), float(close_val), int(volume), int(trade_count), float(vwap)))
        conn.commit()

        c.close()
        conn.close()

        end_time = time.time()
        elapsed_time = end_time - start_time

        logging.info("Elapsed time: ", elapsed_time, "seconds")
        logging.info("Database {} updated".format(table_name))


def update_1T_SPY():
    update_database("1T_SPY", "SPY")

def update_1T_QQQ():
    update_database("1T_QQQ", "QQQ")

def update_5T_SPY():
    update_database("5T_SPY", "SPY")
    
def update_5T_QQQ():
    update_database("5T_QQQ", "QQQ")

def update_1H_SPY():
    update_database("1H_SPY", "SPY")

def update_1H_QQQ():
    update_database("1H_QQQ", "QQQ")

def update_1D_SPY():
    update_database("1D_SPY", "SPY")

def update_1D_QQQ():
    update_database("1D_QQQ", "QQQ")

def update_1W_SPY():
    update_database("1W_SPY", "SPY")

def update_1W_QQQ():
    update_database("1W_QQQ", "QQQ")

def main():
    schedule.every(1).minutes.do(update_1T_SPY)
    schedule.every(1).minutes.do(update_1T_QQQ)
    schedule.every(5).minutes.do(update_5T_SPY)
    schedule.every(5).minutes.do(update_5T_QQQ)
    schedule.every().hour.do(update_1H_SPY)
    schedule.every().hour.do(update_1H_QQQ)
    schedule.every(300).minutes.do(update_1D_SPY)
    schedule.every(300).minutes.do(update_1D_QQQ)
    schedule.every(300).minutes.do(update_1W_SPY)
    schedule.every(300).minutes.do(update_1W_QQQ)

    while True:
        schedule.run_pending()
        time.sleep(1)

#if __name__ == '__main__':
#    main()


