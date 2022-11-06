import pandas as pd

"""Read CSV Files
A simple way to store big data sets is to use CSV files (comma separated files).

CSV files contains plain text and is a well know format that can be read by everyone including Pandas."""

df = pd.read_csv('IMIONA_NADANE_DZIECIOM_W_POLSCE_W_I_POŁOWIE_2022_R._-_IMIĘ_DRUGIE.csv')

#print(df.to_string())

"""
If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:

"""
#print(df)


"""
max_rows
The number of rows returned is defined in Pandas option settings.

You can check your system's maximum rows with the pd.options.display.max_rows statement.
"""

print(pd.options.display.max_rows)

"""
In my system the number is 60, which means that if the DataFrame contains more than 60 rows, the print(df) 
statement will return only the headers and the first and last 5 rows.

You can change the maximum rows number with the same statement.
"""

pd.options.display.max_rows = 9999

print(df)
