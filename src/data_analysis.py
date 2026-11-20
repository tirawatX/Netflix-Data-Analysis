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


def analyze_movie_duration_stats(df):

    # Select Movie duration only
    movie_duration = df.loc[
        df["type"] == "Movie",
        "duration_int"
    ].dropna()

    # Calculate statistics
    mean_duration = movie_duration.mean()
    median_duration = movie_duration.median()
    mode_duration = movie_duration.mode()

    print("\n========== MOVIE DURATION STATISTICS ==========")

    print("Mean:", round(mean_duration, 2))
    print("Median:", median_duration)
    print("Mode:", mode_duration.tolist())

    return {
        "mean": mean_duration,
        "median": median_duration,
        "mode": mode_duration.tolist()
    }


def analyze_movie_outliers(df):

    movie_duration = df.loc[
        df["type"] == "Movie",
        "duration_int"
    ].dropna()

    # Calculate Quartiles
    q1 = movie_duration.quantile(0.25)
    q3 = movie_duration.quantile(0.75)

    # Calculate IQR
    iqr = q3 - q1

    # Calculate boundaries
    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)

    # Find outliers
    outliers = movie_duration[
        (movie_duration < lower_bound) |
        (movie_duration > upper_bound)
    ]

    print("\n========== OUTLIER ANALYSIS ==========")

    print("Q1:", q1)
    print("Q3:", q3)
    print("IQR:", iqr)

    print("Lower Bound:", lower_bound)
    print("Upper Bound:", upper_bound)

    print("Outlier Count:", len(outliers))
    print("Outlier Samples:")
    print(outliers.sort_values(ascending=False).head(10))

    return outliers


def analyze_genres(df):

    print("\n========== GENRE ANALYSIS ==========")

    # Split genres
    genres = df["listed_in"].str.split(", ")

    # Expand genres into separate rows
    all_genres = genres.explode()

    # Count each genre
    genre_counts = all_genres.value_counts()

    print("\nTop 10 Genres:")
    print(genre_counts.head(10))

    return genre_counts