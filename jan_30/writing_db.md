

```python
import sqlite3
import wget
import re
# import sqlite3 as sq3
```


```python
conn = sqlite3.connect('etftodb.db')
c = conn.cursor()
```


```python
def create_db():
    c.execute('''CREATE TABLE 'holdings' (
                'ticker' VARCHAR,
                'comapny_name' VARCHAR,
                'index_weight' VARCHAR,
                'last_price' INTEGER,
                'change_price' VARCHAR,
                'percentage_change' VARCHAR,
                'volume' INTEGER,
                'lowhigh' VARCHAR,
                PRIMARY KEY ('ticker')
        )''')

# comment out after creating db
#     conn.commit()
# create_db()

```


```python
def spdrHoldings(string):
    data = []
    file_url = 'http://www.sectorspdr.com/sectorspdr/IDCO.Client.Spdrs.Holdings/Export/ExportCsv?symbol='
    etf = wget.download(file_url + string)

    with open(etf,'r',errors='replace') as holdings:
        for line in holdings.readlines()[2:]:
            split_line = line.replace('"','').strip().split(',')[:-1]
            if "K" in split_line[6]:
                split_line[6] = int(float(re.sub('["".KM]', '', split_line[6])))*1000
            elif "M" in split_line[6]:
                split_line[6] = int(float(re.sub('["".KM]', '', split_line[6])))*1000000
            split_line[3] = int(float(re.sub('[""]', '', split_line[3])))

            data.append(list(split_line))
    

        return data
```


```python
def insert_data_in_db():
    data = spdrHoldings("XLF")
    print(data[1])
    
    for ticker, comapny_name, index_weight, last_price, change_price, percentage_change, volume, lowhigh, in data:
        new_data = (ticker, comapny_name, index_weight, last_price, change_price, percentage_change, volume, lowhigh)
        c.execute('INSERT INTO holdings VALUES(?,?,?,?,?,?,?,?)', new_data)
        conn.commit()
    conn.close()

insert_data_in_db()
```

    ['JPM', 'JP Morgan Chase & Co', '10.70%', 86, '-0.90', '-1.04%', 1366000000, '52.50 - 88.17']



```python

```
