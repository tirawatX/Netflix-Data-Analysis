import pandas as pd


def analyze_release_year(df):

    print("\n========== CONTENT BY RELEASE YEAR ==========")

    release_year_counts = (
        df["release_year"]
        .value_counts()
        .sort_values(ascending=False)
    )

    print("\nTop 10 Release Years:")
    print(release_year_counts.head(10))

    return release_year_counts

def analyze_content_added_by_year(df):

    print("\n========== CONTENT ADDED BY YEAR ==========")

    content_by_year = (
        df.groupby("year_added")
        .size()
        .sort_values(ascending=False)
    )

    print("\nTop 10 Years:")
    print(content_by_year.head(10))

    return content_by_year