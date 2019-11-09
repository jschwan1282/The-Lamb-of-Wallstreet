import pandas as pd

# load data files
data = pd.read_csv("../Data/FINALmerged.CSV")
words = pd.read_csv("../Data/FINALword_count.CSV")

#create lists
t_dates = []
likes = []
retweets = []
num_tweets = []
adj_close = []
t_value = []
x = 0

# sort through rows of text files and match words in text column aggign predetmined value base on how many keywords are in tweet.
for index, row in data.iterrows():
    t_dates.append(row['Date'])
    likes.append(row['likes'])
    retweets.append(row['retweets'])
    num_tweets.append(1)
    adj_close.append(row[' Close'])
    for index, i in words.iterrows():
        try:
            if i['Word'] in row['text']:
                x = x + i['Count']
            else:
                x = x + 0
        except:
            print(f'nul value{i}')
    t_value.append(x)
    x=0
    

df = pd.DataFrame({
        'date': t_dates,
        'likes' : likes,
        'retweets': retweets,
        'total_tweets': num_tweets,
        'adj_close': adj_close,
        't_value'  : t_value,
})
   
date_group = df.groupby()


df.to_csv('../data/word_values.csv', index=False)