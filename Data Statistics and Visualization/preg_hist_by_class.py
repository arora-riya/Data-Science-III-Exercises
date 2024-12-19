# Question-5

import pandas as pd
import matplotlib.pyplot as plt

diabetes_data = pd.read_csv("pima-indians-diabetes.csv")

grouped_data = diabetes_data.groupby('class')

# Histogram for class 0

plt.hist(grouped_data.get_group(0)['pregs'], bins = range(max(diabetes_data['pregs'])))
plt.ylabel("Frequency")
plt.xlabel("Number of times pregnant")
plt.xticks(range(max(diabetes_data['pregs'])))
plt.title("Histogram for 'pregs' - Class = 0")
plt.show()

# Histogram for class 1

plt.hist(grouped_data.get_group(1)['pregs'], bins = range(max(diabetes_data['pregs'])), color = 'pink')
plt.ylabel("Frequency")
plt.xlabel("Number of times pregnant")
plt.xticks(range(max(diabetes_data['pregs'])))
plt.title("Histogram for 'pregs' - Class = 1")
plt.show()