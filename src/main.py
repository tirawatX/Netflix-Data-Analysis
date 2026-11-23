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
from data_analysis import (
    analyze_release_year,
    analyze_content_added_by_year,
    analyze_movie_duration_stats,
    analyze_movie_outliers,
    analyze_genres,
    analyze_countries
)
from data_visualization import (
    plot_content_added_by_year,
    plot_content_type,
    plot_movie_duration_distribution,
    plot_movie_duration_boxplot,
    plot_top_genres,
    plot_top_countries
)

from data_loader import load_raw_data


def main():

    # Load dataset
    df = load_raw_data()

    # Display dataset information
    print("========== DATA LOADING ==========")

    print("Dataset loaded successfully!")
    print("Shape:", df.shape)

    print("\nFirst 5 Rows:")
    print(df.head())


if __name__ == "__main__":
    main()



if __name__ == "__main__":
    main()
