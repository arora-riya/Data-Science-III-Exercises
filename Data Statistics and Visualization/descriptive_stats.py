# Question-1
# Mean, median, mode, minimum, maximum and standard deviation for all the attributes excluding the attribute ‘class’.

import pandas as pd
import matplotlib.pyplot as plt

diabetes_data = pd.read_csv("pima-indians-diabetes.csv")

print("Mean Values are:")
print(diabetes_data.loc[::,'pregs':'Age'].mean())

print()

print("Median Values are:")
print(diabetes_data.loc[::,'pregs':'Age'].median())

print()

'''
print("Modal Values are:")
print(diabetes_data.loc[::,'pregs':'Age'].mode())'''

print()

print("Minimum Values are:")
print(diabetes_data.loc[::,'pregs':'Age'].min())

print()

print("Maximum Values are:")
print(diabetes_data.loc[::,'pregs':'Age'].max())

print()
print("Standard Deviation Values are:")
print(diabetes_data.loc[::,'pregs':'Age'].std())