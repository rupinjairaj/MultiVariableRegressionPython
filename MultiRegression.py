#!usr/bin/python

import pandas as pd

b_data = pd.read_csv('Data/basketball.csv')

# Obtaining the summary of the data set
print b_data.describe()

# Pearson correlation
print b_data.corr()