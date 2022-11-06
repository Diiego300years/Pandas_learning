import pandas as pd


####################################
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
print(pd.__version__)

#########################




"""
DataFrames
Data sets in Pandas are usually multi-dimensional tables, called DataFrames.

Series is like a column, a DataFrame is the whole table.
"""

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)



"""
What is a DataFrame?
A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, 
or a table with rows and columns.
"""

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df)

"""
Locate Row
As you can see from the result above, the DataFrame is like a table with rows and columns.

Pandas use the loc attribute to return one or more specified row(s)

"""
#refer to the row index:
print(df.loc[0])
# to pokazuje pierwszy wiersz tylko

print(df.loc[[0, 1]])
#to pokazuje normalnie ponieważ jest w podwójnych [[]]
print(df.loc[1])  # nie da się dwoch do nawiasu



"""
With the index argument, you can name your own indexes.
"""

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df)

"""
Locate Named Indexes
Use the named index in the loc attribute to return the specified row(s).
"""

#refer to the named index:
print(df.loc["day2"])


"""
Load a comma separated file (CSV file) into a DataFrame:

import pandas as pd

df = pd.read_csv('data.csv')

print(df)
print(df.to_string()) 
"""




