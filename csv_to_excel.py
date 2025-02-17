import pandas as pd

# Define file paths
csv_file_path = "C:/Users/eyup5/Desktop/Erdinç Hoca/firmquarter_2022q1.csv"
excel_file_path = "C:/Users/eyup5/Desktop/Erdinç Hoca/firmquarter_2022q1.xlsx"

# Attempt to load the CSV with the correct separator
try:
    df = pd.read_csv(csv_file_path, encoding='utf-8', sep='\t', engine='python', on_bad_lines='skip')  # Use tab separator
except UnicodeDecodeError:
    df = pd.read_csv(csv_file_path, encoding='ISO-8859-1', sep='\t', engine='python', on_bad_lines='skip')

# Save it as an Excel file
df.to_excel(excel_file_path, index=False, engine='openpyxl')

print(f"Excel file saved at: {excel_file_path}")
