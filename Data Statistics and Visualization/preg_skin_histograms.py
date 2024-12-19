# Question-3

import pandas as pd
import matplotlib.pyplot as plt

diabetes_data = pd.read_csv("pima-indians-diabetes.csv")

# Histogram for 'preg'

plt.hist(diabetes_data['pregs'], bins = range(max(diabetes_data['pregs'])))
plt.ylabel("Frequency")
plt.xlabel("Number of times pregnant")
plt.xticks(range(max(diabetes_data['pregs'])))
plt.title("Histogram for the Attribute 'pregs'")
plt.show()

# Histogram for 'skin'

plt.hist(diabetes_data['skin'], bins = range(0, max(diabetes_data['skin']), 5), color = 'pink')
plt.ylabel("Frequency")
plt.xlabel("Triceps skin fold thickness (mm)")
plt.xticks(range(0, max(diabetes_data['skin']), 5))
plt.title("Histogram for the Attribute 'skin'")
plt.show()


