
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np
# Generate random data
np.random.seed(42) # Set a seed for reproducibility
# Create a DataFrame with random data 
data = pd.DataFrame({
'variable1': np.random.normal(0, 1, 1000),
'variable2': np.random.normal(2, 2, 1000) + 0.5 * np.random.normal(0, 1, 1000),
'variable3': np.random.normal(-1, 1.5, 1000),
'category': pd.Series(np.random.choice(['A', 'B', 'C', 'D'], size=1000, p=[0.4, 0.3, 0.2, 0.1]), 
dtype='category')
})
# Create a scatter plot to visualize the relationship between two variables 
plt.figure(figsize=(10, 6))
plt.scatter(data['variable1'], data['variable2'], alpha=0.5) 
plt.title('Relationship between Variable 1 and Variable 2', fontsize=16) 
plt.xlabel('Variable 1', fontsize=14)
plt.ylabel('Variable 2', fontsize=14) 
plt.show()
# Create a bar chart to visualize the distribution of a categorical variable 
plt.figure(figsize=(10, 6))
sns.countplot(x='category', data=data) 
plt.title('Distribution of Categories', fontsize=16) 
plt.xlabel('Category', fontsize=14) 
plt.ylabel('Count', fontsize=14) 
plt.xticks(rotation=45)
plt.show()
# Create a heatmap to visualize the correlation between numerical variables 
plt.figure(figsize=(10, 8))
numerical_cols = ['variable1', 'variable2', 'variable3'] 
sns.heatmap(data[numerical_cols].corr(), annot=True, cmap='coolwarm') 
plt.title('Correlation Heatmap', fontsize=16)
plt.show()
