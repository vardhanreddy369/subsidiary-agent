import pandas as pd

# Read the sas7bdat file
file_path = 'subs_all.sas7bdat'
print(f"Reading {file_path}...")
try:
    df = pd.read_sas(file_path, format='sas7bdat')
    print(f"Shape: {df.shape}")
    print(df.head())
    print("\nColumns and Dtypes:")
    print(df.dtypes)
except Exception as e:
    print(f"Error reading with pandas: {e}")
