import boto3
import pandas as pd

def validate_data(df):
    if df.empty:
        raise Exception("Dataframe is empty")

    if df["bitcoin_price_usd"].isnull().sum() > 0:
        raise Exception("Null values found in bitcoin_price_usd")

    print("Data validation passed")