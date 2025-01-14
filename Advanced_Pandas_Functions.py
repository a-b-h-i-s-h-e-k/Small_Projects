'''
# GroupBy
-> GroupBy allows you to group together rows that share the same value in one or 
more columns and then perform an operation on each group. It can be anything 
from aggregation (e.g., sum, mean) to transformation (e.g., standardizing data 
within a group) or filtration (e.g., removing data that does not meet a 
certain condition).
'''

import pandas as pd

# sample dataframe
df = pd.DataFrame({
    'A': ["Delhi","Mumbai", "Delhi", "Mumbai"],
    'B': [1, 2, 3, 4],
    'C': [2.0, 5., 8., 1.] 
})

# grouping by column 'A' and suming up the other columns
grouped = df.groupby('A').sum()
print(grouped)

'''
-> Use GroupBy for segmenting the dataset into groups and applying calculations 
for each group separately, such as summarizing sales data by region or 
calculating average scores by student groups.
'''


'''
# Pivot Tables
-> A pivot table is a data summarization tool frequently used in data processing. 
Pandas pivot_table can automatically sort, count, and total the data stored in one 
DataFrame or Series and is particularly useful for quickly summarizing data and 
highlighting important aspects.
'''

import numpy as np
pivot = pd.pivot_table(df, values='C', index=['A'], aggfunc = np.sum)
print(pivot)

'''
-> Use pivot_table when you need to create a spreadsheet-style pivot table as a 
DataFrame. It’s particularly useful for summarizing and analyzing data to see 
comparisons, patterns, and trends in data.
'''

'''
# Multi-Indexing
-> Pandas support multi-level indexing, or hierarchical indexing, which allows you to 
store and manipulate data with an arbitrary number of dimensions in lower 
dimensional data structures like Series (1D) and DataFrame (2D).
'''

# creating a dataframe with multi-index
index = pd.MultiIndex.from_tuples([('Delhi', 'one'), ('Delhi', 'two'),
                                   ('Mumbai', 'one'), ('Mumbai', 'two')],
                                  names=['first', 'second'])
df_multi = pd.DataFrame(np.random.randn(4,2), index = index, columns = ['A', 'B'])
print(df_multi)

'''
-> Use multi-indexing when you need to work with data that can be categorized by 
two or more keys per data point. It is especially useful for grouping data into 
categories and subcategories.
'''

'''
# Merging, Joining, and Concatenating
-> These functions are used to combine different DataFrames together. Merge is for 
combining data on columns or indices, Join is for combining data on a key column 
or an index, and Concat is for appending dataframes one below the 
other or side by side.

-> Use merge when you need database-style joining of columns, use join for 
combining data on a key index or column, and use concat for stacking 
DataFrames vertically or horizontally.

# Data Transformation with apply() and map()
-> apply() allows you to apply a function along an axis of the DataFrame or on a 
Series. map() is a Series method used to substitute each value in a Series with 
another value.

'''

# Using apply()
df['B'] = df['B'].apply(lambda x: x * 2)

# using map() for a series
df['A'] = df['A'].map({'Delhi': 'New Delhi', 'Mumbai': 'Bombay'})

'''
-> Use apply() for applying a function across rows/columns of a DataFrame or on a 
Series, and use map() for element-wise transformations and substitutions in a Series.
'''

'''
# Query Function
-> The query() function in Pandas allows you to filter a DataFrame using a query 
expression passed as a string. This method offers a more readable syntax for 
filtering data compared to traditional boolean indexing, especially for complex 
conditions. It can be particularly useful when working with large DataFrames and 
performing dynamic data filtering operations.
''' 

import pandas as pd

# sample dataframe
df = pd.DataFrame({
    'A': range(1, 6),
    'B': range(10, 60, 10),
    'C': ['Delhi', 'Mumbai', 'Delhi', 'Mumbai', 'Delhi']
})

# using query() to filter rows
filtered_df = df.query('(A > 2) & (C == "Delhi")')

print(filtered_df)

'''
-> Use the query() function when you need to perform filtering operations on a 
DataFrame and prefer a concise, readable syntax. It’s especially useful in 
situations where the filter conditions are complex or when you’re dynamically 
constructing query strings based on user input or program logic.
'''

