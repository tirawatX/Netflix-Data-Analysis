import pandas as pd
from pathlib import Path

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


def inspect_date_column(df):

    print("\n========== DATE COLUMN INSPECTION ==========")

    print("Data Type:")
    print(df["date_added"].dtype)

    print("\nSample Data:")
    print(df["date_added"].head(10))

    print("\nMissing Values:")
    print(df["date_added"].isnull().sum())

def convert_date_column(df):

    # Create a copy
    df_clean = df.copy()

    # Convert string to datetime
    df_clean["date_added"] = pd.to_datetime(
        df_clean["date_added"].str.strip(),
        format="%B %d, %Y",
        errors="coerce"
    )

    return df_clean

def extract_date_features(df):

    # Create a copy
    df_clean = df.copy()

    # Extract year
    df_clean["year_added"] = df_clean["date_added"].dt.year

    # Extract month
    df_clean["month_added"] = df_clean["date_added"].dt.month

    # Extract day
    df_clean["day_added"] = df_clean["date_added"].dt.day

    return df_clean

def inspect_duration(df):

    print("\n========== DURATION INSPECTION ==========")

    print("\nData Type:")
    print(df["duration"].dtype)

    print("\nSample Data:")
    print(df[["type", "duration"]].head(10))

    print("\nMissing Values:")
    print(df["duration"].isnull().sum())

    print("\nDuration Units:")
    print(df["duration"].str.extract(r"([A-Za-z]+)$")[0].value_counts())


def extract_duration_features(df):

    # Create a copy
    df_clean = df.copy()

    # Extract numeric duration
    df_clean["duration_int"] = (
        df_clean["duration"]
        .str.extract(r"(\d+)")
        .astype("Int64")
    )

    # Extract duration unit
    df_clean["duration_unit"] = (
        df_clean["duration"]
        .str.extract(r"([A-Za-z]+)$")[0]
    )

    # Standardize duration units
    df_clean["duration_unit"] = (
        df_clean["duration_unit"]
        .replace({
            "Season": "Seasons"
        })
    )

    return df_clean



def save_cleaned_data(df, output_path):

    # Convert output path to Path object
    output_path = Path(output_path)

    # Create parent folder if it does not exist
    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Save DataFrame to CSV
    df.to_csv(output_path, index=False)

    print("\nDataset saved successfully!")
    print("Output:", output_path)
