

```python
import requests
```


```python
#Creating a wrapper with requests
def company_search(ticker):
    lookup_url = "http://dev.markitondemand.com/Api/v2/Lookup/json?input="
    r = requests.get(lookup_url + ticker)
    print(r.json())
company_search("aapl")
```

    [{'Exchange': 'NASDAQ', 'Name': 'Apple Inc', 'Symbol': 'AAPL'}, {'Exchange': 'NASDAQ', 'Name': 'AAPL ALPHA INDEX', 'Symbol': 'AVSPY'}, {'Exchange': 'NASDAQ', 'Name': 'NAS OMX Alpha   AAPL vs. SPY  Settle', 'Symbol': 'AIX'}]



```python
#Creating a wrapper with requests
def get_quote(ticker):
        quote_url = "http://dev.markitondemand.com/Api/v2/Quote/json?symbol="
        r = requests.get(quote_url + ticker)
        print(r.json())
get_quote("aapl")
```

    {'MarketCap': 639508160080, 'LastPrice': 121.63, 'Symbol': 'AAPL', 'Low': 120.66, 'Status': 'SUCCESS', 'ChangeYTD': 115.82, 'Open': 120.93, 'ChangePercent': -0.262402624026246, 'Timestamp': 'Mon Jan 30 00:00:00 UTC-05:00 2017', 'Change': -0.320000000000007, 'Name': 'Apple Inc', 'High': 121.63, 'Volume': 30279966, 'MSDate': 42765, 'ChangePercentYTD': 5.01640476601623}



```python

```
