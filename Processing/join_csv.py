import pandas as pd
import datetime as dt

df = pd.read_csv('cleanedtweets.csv', encoding='utf-8')
stock = pd.read_csv('NTFLX.csv', encoding='utf-8')

stock_close = stock[['Date', ' Close']]

df['Date'] = pd.to_datetime(df['timestamp']).dt.strftime('%m/%d/%Y')
stock['Date'] = pd.to_datetime(stock['Date']).dt.date
df.drop('timestamp', axis=1, inplace=True)

merged = pd.merge(left = df, right = stock_close, how = 'right', on="Date")

merged.to_csv('FINALmerged.csv', index=False)