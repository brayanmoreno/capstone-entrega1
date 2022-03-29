def top_users(df):
    return df['user'].value_counts().index.tolist()[:10]
