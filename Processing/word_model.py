import pandas as pd


file = pd.read_csv("Data/FINALmerged.CSV")





rename = file({'likes': 'total_likes', 'retweets': 'total_retweets', 'text': 'tcount'})