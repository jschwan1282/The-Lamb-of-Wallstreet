import pandas as pd
from os import walk
import os
import datetime as dt

#get files names in directory
f = []
for (dirpath, dirnames, filenames) in walk('../Data/Data Staging'):
    f.extend(filenames)
    break

#strip file extentions for file names
f_s = []

for row in f:
    words = row.split('.')
    f_s.append(words[0])



#process each file in directory
for row in f_s:
    print(row)
    clean = pd.read_json(f"../data/Data Staging/{row}.json")
    clean['timestamp'] = pd.to_datetime(clean['timestamp']).dt.date
    final = clean[['timestamp','likes','retweets','text']]

    final.to_csv(f"../data/clean/{row}.csv", index=False)