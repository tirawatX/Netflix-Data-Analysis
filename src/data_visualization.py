import matplotlib.pyplot as plt


def plot_content_added_by_year(df):

    # Group content by year
    content_by_year = (
        df.groupby("year_added")
        .size()
        .sort_index()
    )

    # Create bar chart
    plt.figure(figsize=(10, 5))

    plt.bar(
        content_by_year.index,
        content_by_year.values
    )

    # Add chart title and labels
    plt.title("Netflix Content Added by Year")
    plt.xlabel("Year")
    plt.ylabel("Number of Content")

    # Display grid
    plt.grid(axis="y", alpha=0.3)

    # Show chart
    plt.tight_layout()
    plt.show()


def plot_content_type(df):

    content_counts = df["type"].value_counts()

    plt.figure(figsize=(8, 5))

    plt.bar(
        content_counts.index,
        content_counts.values
    )

    plt.title("Netflix Content Type Distribution")
    plt.xlabel("Content Type")
    plt.ylabel("Number of Content")

    plt.grid(axis="y", alpha=0.3)

    plt.tight_layout()
    plt.show()

def plot_movie_duration_distribution(df):

    # Select Movie only
    movie_duration = df.loc[
        df["type"] == "Movie",
        "duration_int"
    ].dropna()

    # Convert to numeric array
    movie_duration = movie_duration.to_numpy(dtype=float)

    # Create Histogram
    plt.figure(figsize=(10, 5))

    plt.hist(
        movie_duration,
        bins=20,
        edgecolor="black"
    )

    # Add title and labels
    plt.title("Distribution of Netflix Movie Duration")
    plt.xlabel("Duration (Minutes)")
    plt.ylabel("Number of Movies")

    plt.grid(axis="y", alpha=0.3)

    plt.tight_layout()
    plt.show()