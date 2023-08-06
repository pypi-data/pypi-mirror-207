import pandas as pd

def preprocess(df):
    df.index =  pd.to_datetime(df.index, utc=False)
    df = df.rename_axis('DateTime')
    df = df.rename(columns={"value":"Price"})
    df['Week'] = df.index.isocalendar().week
    df['Day'] = df.index.day
    df["Hour"] = df.index.hour

    # Calculate the daily average price and store it in a new DataFrame
    daily_avg = df.resample('D')['Price'].mean()

    df,daily_avg
    # Merge the two DataFrames using the DateTime index with a left join
    merged_df = pd.merge(df, daily_avg, left_index=True, right_index=True, how='left', suffixes=('', '_daily_AVG'))

    # Forward fill the missing values in the 'EXXA Price_daily' column
    merged_df['Price_daily_AVG'].fillna(method='ffill', inplace=True)
    return merged_df

def add_priceRating(df):
    # Assuming your dataframe is called df
    df['rating'] = df['Price'] - df['Price_daily_AVG']
    df['rating_rank'] = df.groupby(df.index.date)['rating'].rank(ascending=True)-1
    return df
