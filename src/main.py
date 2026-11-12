import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from data_cleaning import (
    analyze_missing_values,
    clean_missing_values
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


if __name__ == "__main__":
    main()
