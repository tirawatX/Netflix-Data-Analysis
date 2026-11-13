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

def analyze_duplicates(df):

    # Count duplicate rows
    duplicate_count = df.duplicated().sum()

    # Show duplicate rows
    duplicate_rows = df[df.duplicated(keep=False)]

    print("Total Duplicate Rows:", duplicate_count)

    print("\nDuplicate Data:")
    print(duplicate_rows)

    return duplicate_count


def remove_duplicates(df):

    # Create a copy
    df_clean = df.copy()

    # Count duplicates before removing
    duplicates_before = df_clean.duplicated().sum()

    # Remove duplicate rows
    df_clean = df_clean.drop_duplicates()

    # Count duplicates after removing
    duplicates_after = df_clean.duplicated().sum()

    print("Duplicates Before:", duplicates_before)
    print("Duplicates After:", duplicates_after)

    return df_clean