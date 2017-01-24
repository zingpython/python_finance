import pandas as pd 
import pandas_datareader.data as web
import matplotlib.pyplot as plt 
# from pandas.io.data import DataReader
# from pandas.io import data, wb
import datetime
from datetime import date

start = date(2016,1,1)
end = date(2017,1,20)

# stock_price = web.DataReader("TWTR", "yahoo", start, end)

stock_price = pd.read_csv("table2.csv", parse_dates = True, index_col=0)

print(stock_price.tail(20))

stock_price["MA"] = stock_price["Adj Close"].rolling(window=10).mean()
print(stock_price[["Adj Close","MA"]].tail())

# stock_price.dropna(inplace=True)
# print(stock_price[["Adj Close", "MA"]].tail())

price_fig = plt.subplot2grid((6,1),(0,0), rowspan=5, colspan=1)
volume_fig = plt.subplot2grid((6,1),(5,0), rowspan=1, colspan=1, sharex=price_fig)

price_fig.plot(stock_price.index, stock_price['Adj Close'])
price_fig.plot(stock_price.index, stock_price['MA'])
volume_fig.bar(stock_price.index, stock_price['Volume'])

# stock_price["Adj Close"].plot()
plt.show()


# # print()















