import pandas as pd

"""
Data of Wrong Format
Cells with data of wrong format can make it difficult, or even impossible, to analyze data.

To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.
"""
"""
Let's try to convert all cells in the 'Date' column into dates.
Pandas has a to_datetime() method for this:
"""

df = pd.read_csv('Arkusz kalkulacyjny bez tytułu - Arkusz1.csv')
print(df)
#df['Date'] = pd.to_datetime(df['Date'])

print(df.to_string())