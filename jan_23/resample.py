import pandas as pd 
import pandas_datareader.data as web
import matplotlib.pyplot as plt 
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates


import datetime
from datetime import date

start = date(2016,1,1)
end = date(2017,1,20)

stock_price = web.DataReader("TWTR", "yahoo", start, end)


ten_days = stock_price['Adj Close'].resample('10D').ohlc()
stock_volume = stock_price['Volume'].resample('10D').sum()
print(ten_days.head())

ten_days.reset_index(inplace=True)

ten_days["Date"] = ten_days["Date"].map(mdates.date2num)

price_fig = plt.subplot2grid((6,1),(0,0), rowspan=5, colspan=1)
volume_fig = plt.subplot2grid((6,1),(5,0), rowspan=1, colspan=1, sharex=price_fig)

price_fig.xaxis_date()
candlestick_ohlc(price_fig, ten_days.values, width=5)
volume_fig.fill_between(stock_volume.index.map(mdates.date2num), stock_volume.values, 0)

plt.show()

# print(ten_days.head())




















