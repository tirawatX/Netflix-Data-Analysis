
import pandas as pd
from pathlib import Path


# Get project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent


def load_raw_data():

    # Build dataset path
    file_path = PROJECT_ROOT / "data" / "raw" / "netflix_titles.csv"

    # Check whether file exists
    if not file_path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {file_path}"
        )

    # Load CSV
    df = pd.read_csv(file_path)

    return df
