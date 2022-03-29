def top_tweets(df):
    return df.sort_values('retweetCount', ascending=[False]).head(10)
