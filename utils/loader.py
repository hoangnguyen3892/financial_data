"""Technical Indicators"""

"""
This is used to load data from server and create dataframe.
Note: We use date as index to access rows of dataframe. Date is arranged in chronological order.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import quandl

quandl.ApiConfig.api_key = 'o-yXuCnVqzcxKcUzc6vb'



def get_data(ticker, start, end):
    # Load data from website
    data = quandl.get_table('WIKI/PRICES', ticker = ticker, date = { 'gte': start, 'lte': end }, paginate=True)
    data.columns = ['Ticker', 'Date', 'Open', 'High', 'Low', 'Close', 
                    'Volume', 'Ex_dividend', 'Split_ratio', 'Adj_open',
                    'Adj_high', 'Adj_low', 'Adj_close', 'Adj_volume']
    
    # Parse date
    #cols = ['Date', 'Ticker', 'Adj_close']
    #data = data[cols]
    data = data.set_index('Date')
    pd.to_datetime(data.index)
    return data


def get_selected_data(ticker_list, start, end):
    # Load data from website
    data = quandl.get_table('WIKI/PRICES', ticker = ticker_list, date = { 'gte': start, 'lte': end }, paginate=True)
    data.columns = ['Ticker', 'Date', 'Open', 'High', 'Low', 'Close', 
                    'Volume', 'Ex_dividend', 'Split_ratio', 'Adj_open',
                    'Adj_high', 'Adj_low', 'Adj_close', 'Adj_volume']
    
    # Keep useful columns
    cols = ['Date', 'Ticker', 'Adj_close']
    data = data[cols]
    data = data.set_index('Date')
    pd.to_datetime(data.index)

    # Create new dataframe
    groupByCase = data.groupby(['Ticker'])
    stock_dict = {}
    for name, group in groupByCase:
        stock_dict[name] = group['Adj_close']
    df = pd.DataFrame(stock_dict)
    return df


