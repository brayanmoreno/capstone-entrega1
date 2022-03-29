def top_tweets(df):
    df.sort_values('retweetCount', ascending=[False]).head(10)
