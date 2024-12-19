# Question-2
import pandas as pd
import matplotlib.pyplot as plt

diabetes_data = pd.read_csv("pima-indians-diabetes.csv")

# Scatter plot between 'Age' and other attributes

diabetes_data = diabetes_data.sort_values('Age')

for attribute in diabetes_data.columns[:-2]:
    plt.scatter(diabetes_data['Age'], diabetes_data[attribute], s = 1.5)
    plt.xlabel("Age")
    plt.ylabel(attribute)
    plt.title(f"Scatter Plot between Age and {attribute}")
    plt.show()
    
# Scatter plot between 'BMI' and other attributes

for attribute in diabetes_data.columns:
    if attribute == 'BMI' or attribute == 'class':
        continue
    plt.scatter(diabetes_data['BMI'], diabetes_data[attribute], s = 1.5, c = 'pink')
    plt.xlabel("BMI")
    plt.ylabel(attribute)
    plt.title(f"Scatter Plot between BMI and {attribute}")
    plt.show()
    
