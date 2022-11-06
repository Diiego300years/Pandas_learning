import pandas as pd
import time

# https://github.com/pandas-dev/pandas

st = time.time()
df = pd.read_csv('IMIONA_NADANE_DZIECIOM_W_POLSCE_W_I_POŁOWIE_2022_R._-_IMIĘ_DRUGIE.csv')
print(df)

print(df.to_string())
print(df.items)
print(df.keys())

end = time.time()

print(end-st)

"""
What is a Series?
A Pandas Series is like a column in a table.

It is a one-dimensional array holding data of any type.

"""

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)
"""
Labels
If nothing else is specified, the values are labeled with their index number. First value has index 0, 
second value has index 1 etc.

This label can be used to access a specified value.
"""

print(myvar[0])


# With the index argument, you can name your own labels.
a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)

# When you have created labels, you can access an item by referring to the label.
print(myvar['y'])


"""
Key/Value Objects as Series
You can also use a key/value object, like a dictionary, when creating a Series.
"""
calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)

#Create a Series using only data from "day1" and "day2":

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)


