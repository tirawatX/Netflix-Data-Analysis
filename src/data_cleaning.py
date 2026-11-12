import pandas as pd


def analyze_missing_values(df):

    missing = df.isnull().sum()

    missing_percent = (
        df.isnull().sum() / len(df)
    ) * 100

    result = pd.DataFrame({
        "Missing Values": missing,
        "Percentage": missing_percent
    })

    result = result.sort_values(
        by="Missing Values",
        ascending=False
    )

    return result

def clean_missing_values(df):

    # Create a copy to protect original data
    df_clean = df.copy()

    # Fill missing values in text columns
    columns_to_fill = [
        "director",
        "cast",
        "country"
    ]

    for column in columns_to_fill:
        df_clean[column] = df_clean[column].fillna("Unknown")

    return df_clean