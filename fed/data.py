import requests
import json
import pandas as pd

def fetch_data(country_code: str):
    try:
        response = requests.get(f"https://api.worldbank.org/v2/country/{country_code}/indicator/NY.GDP.MKTP.CD?date=2000:2022&per_page=70&format=json")
        response.raise_for_status()
        raw = response.json()

        # World Bank API returns metadata and data separately
        data_list = raw[1]  # second item has the actual data records because first is metadata

        # flatten nested json
        df = pd.json_normalize(data_list)
        print("Fetched data:")
        print(df.head())
        return df
    except requests.RequestException as e:
        print("Request error:", e)
        return None

def clean_data(df: pd.DataFrame):
    # keep only what you need
    df_columns = df[["date","value","country.value"]].copy()

    # rename columns
    df_columns.rename(columns={"date": "Year", "value": "GDP", "country.value": "Country"}, inplace=True)

    # convert types
    df_columns["Year"] = pd.to_numeric(df_columns["Year"], errors='coerce')
    df_columns["GDP"] = pd.to_numeric(df_columns["GDP"], errors='coerce')  
    df_columns["Country"] = df_columns["Country"].astype("category")

    # drop missing values
    df_cleaned = df_columns.dropna()
    print("Cleaned data:")
    print(df_cleaned.head())
    return df_cleaned
