import pandas as pd

file_path = 'subs_all.sas7bdat'
print(f"Reading {file_path}...")
df = pd.read_sas(file_path, format='sas7bdat')

# Decode byte strings
for col in ['CIK', 'COMP_NAME', 'SUB_NAME']:
    if df[col].dtype == object:
        df[col] = df[col].apply(lambda x: x.decode('utf-8', errors='ignore').strip() if isinstance(x, bytes) else x)

print("Decoded data preview:")
print(df.head())

# Save a sample to CSV for easy viewing
sample_df = df.sample(n=100, random_state=42)
sample_df.to_csv('subs_sample.csv', index=False)
print("Saved 100 random rows to subs_sample.csv")
