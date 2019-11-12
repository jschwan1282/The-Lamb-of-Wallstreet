import pandas as pd
from os import walk
import os
import datetime as dt

#create lists
f = []
t_dates = []
likes = []
retweets = []
num_tweets = []
# adj_close = []
t_value = []
x = 0

for (dirpath, dirnames, filenames) in walk('../Data/clean'):
    f.extend(filenames)
    break

# load data files
for row in f:
    data = pd.read_csv(f'../Data/clean/{row}')
    words = pd.read_csv('../Data/check_words.csv')
    print(f'working on: {row}')

    # sort through rows of text files and match words in text column aggign predetmined value base on how many keywords are in tweet.
    for index, rows in data.iterrows():
        t_dates.append(rows['timestamp'])
        likes.append(rows['likes'])
        retweets.append(rows['retweets'])
        num_tweets.append(1)
        # adj_close.append(rows[' Close'])
        for index, i in words.iterrows():
            try:
                if i['Word'] in rows['text']:
                    x = x + i['Count']
                else:
                    x = x + 0
            except:
                print(f'null value{i}')
        t_value.append(x)
        x=0
        

df = pd.DataFrame({
    'date': t_dates,
    'likes' : likes,
    'retweets': retweets,
    'total_tweets': num_tweets,
    # 'adj_close': adj_close,
    't_value'  : t_value,
})

df.to_csv(f'../data/clean/final_tweets.csv', index=False)