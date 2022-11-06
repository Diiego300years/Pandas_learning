import pandas as pd

"""
Replace Using Mean, Median, or Mode
A common way to replace empty cells, is to calculate the mean, median or mode value of the column.

Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column

Below mean()
"""
df = pd.read_csv('data.csv')
print(df.to_string())

x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True)
print(df.to_string())

#Mean = the average value (the sum of all values divided by number of values).

"""
Calculate the MEDIAN, and replace any empty values with it:
"""

df = pd.read_csv('data.csv')
x = df["Calories"].median()

df["Calories"].fillna(x, inplace = True)

# Median = the value in the middle, after you have sorted all values ascending- rosnąco.


"""
Calculate the MODE, and replace any empty values with it:
"""
df = pd.read_csv('data.csv')

x = df["Calories"].mode()[0]

df["Calories"].fillna(x, inplace = True)

# Mode = the value that appears most frequently.