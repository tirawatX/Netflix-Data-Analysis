
import sqlite3
import pandas as pd
from pathlib import Path


# Project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent

CSV_PATH = PROJECT_ROOT / "data" / "processed" / "netflix_cleaned.csv"
DB_PATH = PROJECT_ROOT / "data" / "processed" / "netflix.db"


def create_database():

    # Load cleaned dataset
    df = pd.read_csv(CSV_PATH)

    # Connect to SQLite database
    conn = sqlite3.connect(DB_PATH)

    # Create SQL table
    df.to_sql(
        "netflix_titles",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

    print("Database created successfully!")
    print("Rows:", len(df))
    print("Database:", DB_PATH)


if __name__ == "__main__":
    create_database()
