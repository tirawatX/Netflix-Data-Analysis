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
    analyze_content_added_by_year
)
from data_visualization import (
    plot_content_added_by_year,
    plot_content_type,
    plot_movie_duration_distribution
)



def main():

    df = pd.read_csv("data/processed/netflix_cleaned.csv")

    analyze_release_year(df)

    analyze_content_added_by_year(df)

    plot_content_added_by_year(df)

    plot_content_type(df)

    plot_movie_duration_distribution(df)


if __name__ == "__main__":
    main()
