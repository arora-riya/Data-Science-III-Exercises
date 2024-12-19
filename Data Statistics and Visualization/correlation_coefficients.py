# Question-3

import pandas as pd

diabetes_data = pd.read_csv("pima-indians-diabetes.csv")

# Correlation Coefficient of 'Age' with other attributes

print("Correlation Coefficient of 'Age' with: ")
for attribute in diabetes_data.columns[:-2]:
    print(attribute + " =", diabetes_data['Age'].corr(diabetes_data[attribute]))
    
print()

print("Correlation Coefficient of 'BMI' with: ")
for attribute in diabetes_data.columns:
    if attribute == 'BMI' or attribute == 'class':
        continue
    print(attribute + " =", diabetes_data['BMI'].corr(diabetes_data[attribute]))
    