
def validate_dataset(df):

    print("\n========== DATA VALIDATION ==========")

    # 1. Check Dataset Shape
    print("\nDataset Shape:")
    print(df.shape)

    # 2. Check Missing Values
    print("\nTotal Missing Values:")
    print(df.isnull().sum().sum())

    # 3. Check Duplicate Rows
    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    # 4. Check Data Types
    print("\nData Types:")
    print(df.dtypes)

    # 5. Check Required Columns
    required_columns = [
        "title",
        "type",
        "date_added",
        "duration_int",
        "duration_unit"
    ]

    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    print("\nMissing Required Columns:")
    print(missing_columns)

    print("\nValidation Completed!")
