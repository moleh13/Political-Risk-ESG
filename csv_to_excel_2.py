import pandas as pd

# Define file paths
csv_file_path = "C:/Users/eyup5/Desktop/Erdinç Hoca/reprisk_firms.csv"  # Ensure the correct path to your CSV file
excel_file_path = "C:/Users/eyup5/Desktop/Erdinç Hoca/reprisk_firms.xlsx"  # Output file with full path

# Load the CSV file with proper encoding
df = pd.read_csv(csv_file_path, encoding='utf-8')

# Save it as an Excel file
df.to_excel(excel_file_path, index=False, engine='openpyxl')

print(f"Excel file saved at: {excel_file_path}")
