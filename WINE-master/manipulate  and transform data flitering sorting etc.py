Manipulate and transform data using functions like filtering, sorting, and grouping Code

import pandas as pd

iris = pd.read_csv('Iris.csv')

setosa = iris[iris['Species'] == 'setosa'] 
print("Setosa samples:")
print(setosa.head())

sorted_iris = iris.sort_values(by='SepalLengthCm', ascending=False) 
print("\nSorted iris dataset:")
print(sorted_iris.head())

grouped_species = iris.groupby('Species').mean() 
print("\nMean measurements for each species:")
print(grouped_species)
