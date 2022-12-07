import datetime as dt
import pandas as pd
from pandas_datareader import data
import matplotlib.pyplot as plt


# This function reads in closing price data from Yahoo Finance
# using the pandas_datareader library
def get_closing_prices(ticker_dictionary,
                       start=dt.datetime(2021, 1, 2),
                       end=dt.datetime(2021, 12, 31)):

    # Create an empty pandas dataframe
    ticker_dataframe = pd.DataFrame()

    for tick in ticker_dictionary:
        prices = data.DataReader(tick, 'yahoo', start, end)
        closing_prices = prices['Close']
        ticker_dataframe[tick] = closing_prices

    return ticker_dataframe


sample_ticker_dictionary = {'MSFT': 'Microsoft',
                            'AAPL': 'Apple',
                            'QCOM': 'Qualcomm',
                            'KO': 'Coca-Cola',
                            'GOOG': 'Google',
                            'PTR': 'PetroChina'}

# Write your code below here
