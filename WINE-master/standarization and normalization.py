Apply feature-scaling techniques like standardization and normalization to numerical features.

*Wine*

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler

df = pd.read_csv('wine.csv', header=None, usecols=[0, 1, 2], skiprows=1)
df.columns = ['classlabel', 'Alcohol', 'Malic Acid']

print("Original DataFrame:")
print(df)

scaler = MinMaxScaler()
scaled_values = scaler.fit_transform(df[['Alcohol', 'Malic Acid']])
df[['Alcohol', 'Malic Acid']] = scaled_values
print("\nDataFrame after MinMax Scaling:")
print(df)

scaler = StandardScaler()
scaled_standard_values = scaler.fit_transform(df[['Alcohol', 'Malic Acid']])
df[['Alcohol', 'Malic Acid']] = scaled_standard_values
print("\nDataFrame after Standard Scaling:")
print(df)
