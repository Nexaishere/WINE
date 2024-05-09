chi test: hypothesis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import warnings

from scipy import stats
warnings.filterwarnings('ignore')

df = sb.load_dataset('mpg')

print(df)

print(df['horsepower'].describe())
print(df['model_year'].describe())

bins = [0, 75, 150, 240]
ybins = [69, 72, 74, 84]

df['horsepower_new'] = pd.cut(df['horsepower'], bins=bins, labels=['l', 'm', 'h'])
df['modelyear_new'] = pd.cut(df['model_year'], bins=ybins, labels=['t1', 't2', 't3'])

c = df['horsepower_new']
newyear = df['modelyear_new']

print(c)
print(newyear)

df_chi = pd.crosstab(df['horsepower_new'], df['modelyear_new'])
print(df_chi)
print(stats.chi2_contingency(df_chi))
