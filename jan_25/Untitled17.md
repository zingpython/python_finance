

```python
import pandas as pd
import numpy as np
import datetime
from datetime import date
import matplotlib.pyplot as plt
#This is the old way to import DataReader 
#If you use TextEditor and Terminal
#import pandas_datareader.data as web
from pandas.io.data import DataReader
from pandas.io import data, wb
```

    /Users/mclaren/anaconda3/lib/python3.5/site-packages/pandas/io/data.py:33: FutureWarning: 
    The pandas.io.data module is moved to a separate package (pandas-datareader) and will be removed from pandas in a future version.
    After installing the pandas-datareader package (https://github.com/pydata/pandas-datareader), you can change the import ``from pandas.io import data, wb`` to ``from pandas_datareader import data, wb``.
      FutureWarning)
    /Users/mclaren/anaconda3/lib/python3.5/site-packages/pandas/io/wb.py:19: FutureWarning: 
    The pandas.io.wb module is moved to a separate package (pandas-datareader) and will be removed from pandas in a future version.
    After installing the pandas-datareader package (https://github.com/pydata/pandas-datareader), you can change the import ``from pandas.io import data, wb`` to ``from pandas_datareader import data, wb``.
      FutureWarning)



```python
start = date(2014, 1, 1)
end = date.today()
```


```python
portfolio = ["AAPL","MSFT","GE","BAC", "VZ"]
data = pd.DataFrame()
for co in portfolio:
    data[co] = DataReader(co, 'yahoo', start, end)["Adj Close"]
```


```python
(data/data.ix[0] * 100).plot()
plt.show()
```


```python
#Calculating returns
returns = np.log(data/data.shift(1))
returns.tail()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAPL</th>
      <th>MSFT</th>
      <th>GE</th>
      <th>BAC</th>
      <th>VZ</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-01-19</th>
      <td>-0.001752</td>
      <td>-0.003205</td>
      <td>-0.000641</td>
      <td>-0.004429</td>
      <td>0.002103</td>
    </tr>
    <tr>
      <th>2017-01-20</th>
      <td>0.001835</td>
      <td>0.007038</td>
      <td>-0.022029</td>
      <td>0.004870</td>
      <td>0.006852</td>
    </tr>
    <tr>
      <th>2017-01-23</th>
      <td>0.000666</td>
      <td>0.003500</td>
      <td>-0.025881</td>
      <td>-0.003540</td>
      <td>-0.005897</td>
    </tr>
    <tr>
      <th>2017-01-24</th>
      <td>-0.000916</td>
      <td>0.008855</td>
      <td>0.008368</td>
      <td>0.017140</td>
      <td>-0.044677</td>
    </tr>
    <tr>
      <th>2017-01-25</th>
      <td>0.015795</td>
      <td>0.002516</td>
      <td>0.012258</td>
      <td>0.018135</td>
      <td>-0.007008</td>
    </tr>
  </tbody>
</table>
</div>




```python
returns.hist(bins=50)
plt.show()
```


```python
#Since we have significant differences in performance, 
#we have to use 252 trading days to annualize the daily returns 
returns.mean() * 252
```




    AAPL    0.161162
    MSFT    0.202509
    GE      0.064957
    BAC     0.131995
    VZ      0.052840
    dtype: float64




```python
#Building covariance matrix
returns.cov() * 252
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AAPL</th>
      <th>MSFT</th>
      <th>GE</th>
      <th>BAC</th>
      <th>VZ</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>AAPL</th>
      <td>0.056638</td>
      <td>0.024614</td>
      <td>0.015993</td>
      <td>0.020574</td>
      <td>0.010625</td>
    </tr>
    <tr>
      <th>MSFT</th>
      <td>0.024614</td>
      <td>0.054326</td>
      <td>0.019334</td>
      <td>0.025095</td>
      <td>0.014742</td>
    </tr>
    <tr>
      <th>GE</th>
      <td>0.015993</td>
      <td>0.019334</td>
      <td>0.033216</td>
      <td>0.024723</td>
      <td>0.011506</td>
    </tr>
    <tr>
      <th>BAC</th>
      <td>0.020574</td>
      <td>0.025095</td>
      <td>0.024723</td>
      <td>0.071724</td>
      <td>0.010242</td>
    </tr>
    <tr>
      <th>VZ</th>
      <td>0.010625</td>
      <td>0.014742</td>
      <td>0.011506</td>
      <td>0.010242</td>
      <td>0.024588</td>
    </tr>
  </tbody>
</table>
</div>




```python
#We assume that we do not open short position and we divide our money equally divided among 5 stocks
#So we generate 5 random numbers and then normalize them so that values would sum up 100% net oper assets
noa = len(portfolio)
weights = np.random.random(noa)
weights /= np.sum(weights)
weights
```




    array([ 0.01032802,  0.29855077,  0.27292579,  0.32555879,  0.09263663])




```python
#Calculating Expected portfolio return based on the weights
expected_return = np.sum(returns.mean() * weights) * 252
expected_return
```




    0.12771957604844436




```python
#Now lets calculate Expected portfolio variance using our covariance matrix
#we use np.dot -  gets us a product of two matrices
expected_variance = np.dot(weights.T, np.dot(returns.cov() * 252, weights))
expected_variance
```




    0.029973647696510147




```python
#Now we calculate expected standard deviation or volatility 
volatility = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights))) 
volatility
```




    0.17312899149625446




```python
#Monte Carlo simulation to generate random portfolio weight vectors on larger scale
#For every simulated allocation we record the resulting portfolio return and variance
#We assume Risk free is 0
mrets = []
mvols = []
for i in range(2500):
    weights = np.random.random(noa)
    weights /= np.sum(weights)
    mrets.append(np.sum(returns.mean() * weights) * 252)
    mvols.append(np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights ))))
    
mrets = np.array(mrets)
mvols = np.array(mvols)
```


```python
#Lets plot it
plt.figure()
plt.scatter(mvols, mrets, c=mrets / mvols, marker='o')
plt.grid(True)
plt.xlabel('Expected volatility')
plt.ylabel('Expected return')
plt.colorbar(label="Sharpe ratio")
plt.show()
```


```python

```
