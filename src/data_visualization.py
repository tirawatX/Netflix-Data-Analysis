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