import pandas as pd
# Empty cells can potentially give you a wrong result when you analyze data.

"""Remove Rows
One way to deal with empty cells is to remove rows that contain empty cells.
This is usually OK, since data sets can be very big, and removing a few rows will 
not have a big impact on the result."""

df = pd.read_csv('data.csv')
print(pd.DataFrame(df).to_string())
new_df = df.dropna()

#usuwamy 27 wiersz i znika
print(new_df.to_string())

#vNote: By default, the dropna() method returns a new DataFrame, and will not change the original.


"""
If you want to change the original DataFrame, use the inplace = True argument:
"""

df = pd.read_csv('data.csv')

df.dropna(inplace = True)

print(df.to_string())

"""
 Now, the dropna(inplace = True) will NOT return a new DataFrame, 
 but it will remove all rows containing NULL values from the original DataFrame.
"""


"""
Replace Empty Values
Another way of dealing with empty cells is to insert a new value instead.

This way you do not have to delete entire rows just because of some empty cells.

The fillna() method allows us to replace empty cells with a value:
"""
df = pd.read_csv('data.csv')

df.fillna(130, inplace = True)

print(df.to_string())

"""
Replace Only For Specified Columns
The example above replaces all empty cells in the whole Data Frame.

To only replace empty values for one column, specify the column name for the DataFrame:
"""
df = pd.read_csv('data.csv')

df["Calories"].fillna(130, inplace = True)
