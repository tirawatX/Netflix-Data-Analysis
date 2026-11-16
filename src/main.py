import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from data_cleaning import (
    analyze_missing_values,
    clean_missing_values,
    analyze_duplicates,
    remove_duplicates,
    inspect_date_column,
    convert_date_column,
    extract_date_features,
    inspect_duration,
    extract_duration_features,
    save_cleaned_data
)



def main():

    # Load Raw Dataset
    df = pd.read_csv("data/netflix_titles.csv")

    print("\n========== BEFORE CLEANING ==========")
    print(df.isnull().sum())

    # Clean Dataset
    df_clean = clean_missing_values(df)

    print("\n========== AFTER CLEANING ==========")
    print(df_clean.isnull().sum())

    # Verify Original Data
    print("\n========== ORIGINAL DATA CHECK ==========")
    print("Original director missing:",
          df["director"].isnull().sum())

    # Verify Cleaned Data
    print("\n========== CLEANED DATA CHECK ==========")
    print("Cleaned director missing:",
          df_clean["director"].isnull().sum())

    print("\nOriginal Shape:", df.shape)
    print("Cleaned Shape:", df_clean.shape)

    print("\n========== DUPLICATE ANALYSIS ==========")

    duplicate_count = analyze_duplicates(df)

    print("\nTotal Duplicate Rows:", duplicate_count)

    print("\n========== REMOVE DUPLICATES ==========")

    df_no_duplicates = remove_duplicates(df)

    print("\nOriginal Shape:", df.shape)
    print("Cleaned Shape:", df_no_duplicates.shape)

    inspect_date_column(df)
    print("\n========== DATE CONVERSION ==========")

    df_date = convert_date_column(df)

    print("\nBefore Conversion:")
    print(df["date_added"].dtype)

    print("\nAfter Conversion:")
    print(df_date["date_added"].dtype)

    print("\nConverted Sample:")
    print(df_date["date_added"].head(10))

    print("\nMissing Dates:")
    print(df_date["date_added"].isnull().sum())



    df_features = extract_date_features(df_date)

    print(df_features[
        ["date_added", "year_added", "month_added", "day_added"]
    ].head(10))

    print("\nNew Columns:")
    print(df_features.columns.tolist())

    inspect_duration(df)


    print("\n========== DURATION FEATURE ENGINEERING ==========")

    df_duration = extract_duration_features(df)

    print(
        df_duration[
            ["type", "duration", "duration_int", "duration_unit"]
        ].head(15)
    )

    print("\nDuration Units After Cleaning:")
    print(df_duration["duration_unit"].value_counts())

    print("\nMissing Duration:")
    print(df_duration["duration_int"].isnull().sum())


    df_clean = clean_missing_values(df)

    df_clean = remove_duplicates(df_clean)

    df_clean = convert_date_column(df_clean)

    df_clean = extract_date_features(df_clean)

    df_clean = extract_duration_features(df_clean)

    save_cleaned_data(
        df_clean,
        "data/processed/netflix_cleaned.csv"
    )

if __name__ == "__main__":
    main()
