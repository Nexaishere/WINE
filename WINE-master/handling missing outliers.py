handling missing and outliers csv & json

import pandas as pd

def handle_outliers(column, factor=2):
 median_value = column.median()
 upper_threshold = column.mean() + factor * column.std()
 lower_threshold = column.mean() - factor * column.std()
 return column.apply(lambda x: median_value if x >upper_threshold or x <lower_threshold 
else x)

csv_file_path = 'Sales.csv'
df_csv = pd.read_csv(csv_file_path)

json_file_path = 'Sales.json'
df_json = pd.read_json(json_file_path)

print("CSV Data:")
print(df_csv.head())
print("\nJSON Data:")
print(df_json.head())

df_csv_cleaned = df_csv.dropna()
df_json_filled = df_json.fillna(0)

df_csv['Sales'] = handle_outliers(df_csv['Sales'])

filtered_data = df_csv[df_csv['Sales'] > 10]
sorted_data = df_csv.sort_values(by='Sales', ascending=False)
numeric_columns = ['Sales', 'Cost', 'Profit']
grouped_data = df_csv.groupby('Category')[numeric_columns].mean()

print("\nCleaned CSV Data:")
print(df_csv_cleaned.head())
print("\nFilled JSON Data:")
print(df_json_filled.head())
print("\nFiltered Data:")
print(filtered_data.head())
print("\nSorted Data:")
print(sorted_data.head())
print("\nGrouped Data:")
print(grouped_data.head())
