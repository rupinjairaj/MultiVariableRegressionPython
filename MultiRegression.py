#!usr/bin/python

import pandas as pd
import matplotlib.pyplot as plt

b_data = pd.read_csv('Data/basketball.csv')

# Obtaining the summary of the data set
print b_data.describe()

# Pearson correlation
print b_data.corr()

# Plotting the distribution of independent variables with respect to the dependent variables 
## Plotting the distribution b/w height and avg points scored
fig, ax = plt.subplots(1, 1)
ax.scatter(b_data.height, b_data.avg_points_scored)
ax.set_xlabel('height')
ax.set_ylabel('Average points scored per game')
plt.show()

## Plotting the distribution b/w weight and avg points scored
fig, ax = plt.subplots(1, 1)
ax.scatter(b_data.weight, b_data.avg_points_scored)
ax.set_xlabel('weight')
ax.set_ylabel('Average points scored per game')
plt.show()

## Plotting the distribution b/w successful field goals and avg points scored
fig, ax = plt.subplots(1, 1)
ax.scatter(b_data.success_field_goals, b_data.avg_points_scored)
ax.set_xlabel('Success Field Goals')
ax.set_ylabel('Average points scored per game')
plt.show()

## Plotting the distribution b/w successful free throws and avg points scored
fig, ax = plt.subplots(1, 1)
ax.scatter(b_data.success_free_throws, b_data.avg_points_scored)
ax.set_xlabel('Success free throws')
ax.set_ylabel('Average points scored per game')
plt.show()