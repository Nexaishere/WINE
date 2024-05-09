Regression and its types

import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

housing = fetch_california_housing()
housing_df = pd.DataFrame(housing.data, columns=housing.feature_names)
print(housing_df)

housing_df['PRICE'] = housing.target

X = housing_df[['AveRooms']]
y = housing_df['PRICE']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

mse = mean_squared_error(y_test, model.predict(X_test))
r2 = r2_score(y_test, model.predict(X_test))

print("Mean Squared Error (Single Linear Regression):", mse)
print("R-squared (Single Linear Regression):", r2)
print("Intercept (Single Linear Regression):", model.intercept_)
print("Coefficient (Single Linear Regression):", model.coef_)


# Multiple Linear Regression

X = housing_df.drop('PRICE', axis=1)
y = housing_df['PRICE']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nMean Squared Error (Multiple Linear Regression):", mse)
print("R-squared (Multiple Linear Regression):", r2)
print("Intercept (Multiple Linear Regression):", model.intercept_)
print("Coefficients (Multiple Linear Regression):", model.coef_)
