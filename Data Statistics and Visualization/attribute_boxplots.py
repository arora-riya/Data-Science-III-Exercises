# Question-6
# Boxplots for all the attributes excluding class

import pandas as pd
import matplotlib.pyplot as plt

diabetes_data = pd.read_csv("pima-indians-diabetes.csv")

plt.boxplot(diabetes_data.loc[::, : 'Age'], patch_artist = True)
plt.xticks(range(1, 9), diabetes_data.loc[::, : 'Age'].columns)
plt.title("Box-Plots for Various DataFrame Attributes")
plt.grid()
plt.show()

