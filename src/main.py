import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

from streamlit import form
from data_cleaning import (
    clean_missing_values,
    remove_duplicates,
    convert_date_column,
    extract_date_features,
    extract_duration_features,
    save_cleaned_data
)

from data_analysis import (
    analyze_release_year,
    analyze_content_added_by_year,
    analyze_movie_duration_stats,
    analyze_movie_outliers,
    analyze_genres,
    analyze_countries
)
import data_validation
from data_visualization import (
    plot_content_added_by_year,
    plot_content_type,
    plot_movie_duration_distribution,
    plot_movie_duration_boxplot,
    plot_top_genres,
    plot_top_countries
)

from data_validation import validate_dataset

from data_loader import load_raw_data

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent

OUTPUT_PATH = PROJECT_ROOT / "data" / "processed" / "netflix_cleaned.csv"


def main():

    print("\n========== NETFLIX DATA PIPELINE ==========")

    # Step 1: Load Raw Data
    print("\n[1] Loading Raw Data...")

    df = load_raw_data()

    print("Raw Data Shape:", df.shape)

    # Step 2: Clean Missing Values
    print("\n[2] Cleaning Missing Values...")

    df_clean = clean_missing_values(df)

    # Step 3: Remove Duplicates
    print("\n[3] Removing Duplicates...")

    df_clean = remove_duplicates(df_clean)

    # Step 4: Convert Date
    print("\n[4] Converting Date Column...")

    df_clean = convert_date_column(df_clean)

    # Step 5: Extract Date Features
    print("\n[5] Extracting Date Features...")

    df_clean = extract_date_features(df_clean)

    # Step 6: Extract Duration Features
    print("\n[6] Extracting Duration Features...")

    df_clean = extract_duration_features(df_clean)

    # Step 7: Save Processed Data
    print("\n[7] Saving Processed Data...")

    save_cleaned_data(df_clean, OUTPUT_PATH)

    # Final Summary
    print("\n========== PIPELINE SUMMARY ==========")

    print("Original Shape:", df.shape)
    print("Processed Shape:", df_clean.shape)

    print("\nPipeline completed successfully!")

    validate_dataset(df_clean)

if __name__ == "__main__":
    main()
