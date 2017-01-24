import pandas as pd 

stocks = ["IBM", "MSFT", "ORCL", "TWTR"]
prices = [115, 23, 24, 19]

portfolio = list(zip(stocks, prices))

df = pd.DataFrame(data=portfolio, columns=["Stocks","Prices"])

df["New column"] = 5

df.to_csv("portfolio.csv", index=True)

new_file = pd.read_csv("portfolio2.csv",
				index_col="Index",
				names=[
					"Index",
					"Stock",
					"Price",
					"Col 5",
				],
				skiprows=1
	)


df.index = ['a', 'b','c','d']

print(df.loc["b":"d"])






