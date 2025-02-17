import pandas as pd

# Define file paths
firmquarter_csv = "C:/Users/eyup5/Desktop/Erdinç Hoca/firmquarter_2022q1.csv"
reprisk_csv = "C:/Users/eyup5/Desktop/Erdinç Hoca/reprisk_firms.csv"

# Load firmquarter CSV and extract unique ISIN values
try:
    firmquarter_df = pd.read_csv(firmquarter_csv, encoding='utf-8', sep='\t', engine='python')
except UnicodeDecodeError:
    firmquarter_df = pd.read_csv(firmquarter_csv, encoding='ISO-8859-1', sep='\t', engine='python')

# Ensure column name exists
if 'isin' not in firmquarter_df.columns:
    print("Error: 'isin' column not found in firmquarter file.")
    exit()

unique_isin_firmquarter = set(firmquarter_df['isin'].dropna().unique())  # Get unique ISINs

# Load reprisk firms CSV without filtering for uniqueness
try:
    reprisk_df = pd.read_csv(reprisk_csv, encoding='utf-8', sep=',', engine='python')
except UnicodeDecodeError:
    reprisk_df = pd.read_csv(reprisk_csv, encoding='ISO-8859-1', sep=',', engine='python')

# Ensure column name exists
if 'primary_isin' not in reprisk_df.columns:
    print("Error: 'primary_isin' column not found in reprisk file.")
    exit()

# Compare unique firmquarter ISINs against all primary_isin values in reprisk
matching_isins = unique_isin_firmquarter.intersection(set(reprisk_df['primary_isin'].dropna()))

# Print the results
print(f"Total unique ISINs in firmquarter: {len(unique_isin_firmquarter)}")
print(f"Total primary ISINs in reprisk (without filtering uniqueness): {len(reprisk_df['primary_isin'].dropna())}")
print(f"Number of matching ISINs: {len(matching_isins)}")
