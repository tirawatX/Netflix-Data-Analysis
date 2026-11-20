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
    analyze_genres
)
from data_visualization import (
    plot_content_added_by_year,
    plot_content_type,
    plot_movie_duration_distribution,
    plot_movie_duration_boxplot
)



def main():
    df = pd.read_csv("data/processed/netflix_cleaned.csv")

    analyze_movie_duration_stats(df)

    analyze_movie_outliers(df)

    plot_movie_duration_boxplot(df)

    analyze_genres(df)


if __name__ == "__main__":
    main()
