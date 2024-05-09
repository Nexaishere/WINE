Read data from CSV and JSON files into a data frame. 

import pandas as pd
csv_file_path = 'Crescent.csv'
def read_csv_file(file_path):
 try:
  data_frame = pd.read_csv(file_path)
  return data_frame
 except FileNotFoundError:
  print(f"Error: File not found at path '{file_path}'")
csv_data = read_csv_file(csv_file_path)
if csv_data is not None:
  print("CSV Data:")
  print(csv_data)




*json*

import json
json_file_path = 'prac.json'
def read_json_file(file_path):
 with open(file_path, 'r') as file:
        data = json.load(file)
        return data
try:
        json_data = read_json_file(json_file_path)
        print("JSON Data:") 
        print(json.dumps(json_data, indent=2))
except FileNotFoundError:
      print(f"Error: File not found at path '{json_file_path}'")
except json.JSONDecodeError:
      print(f"Error: Invalid JSON format in file at path '{json_file_path}'")
