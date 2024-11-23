'''
# What is Pandas?
--> Pandas is a powerful open-source library in Python that provides 
high-performance data manipulation and analysis tools. It introduces two fundamental 
data structures: Series and DataFrame, which allow data to be organized, 
manipulated, and analyzed in a tabular format similar to spreadsheets 
or databases.

--> Data Science professionals rely on Pandas for several reasons. Firstly, Pandas 
simplifies the process of data handling and manipulation, allowing professionals 
to clean, preprocess, and transform data. 

--> Secondly, Pandas offers powerful tools for data analysis and exploration. 
It provides functions for aggregating data, computing descriptive statistics, handling 
time series data, and working with categorical and textual data.

--> Furthermore, Pandas excels at data integration and preparation. Data Science 
professionals can easily load data from different sources (such as CSV, Excel, 
SQL databases, and more), merge or join datasets, and perform data 
transformations before further analysis.

--> To install Pandas on your Python virtual environment.

    pip install pandas

--> The DataFrame contains information about a group of individuals. Each row 
represents a person, and the columns represent different attributes or 
characteristics of these individuals.

'''

import pandas as pd

data = {'Name': ['Lucky', 'Reem', 'Akshita', 'Diviyanka', 'Karan'],
        'Age': [24, 20, 25, 28, 29],
        'City': ['New Delhi', 'Mumbai', 'Banglore', 'Pune', 'Chennai'],
        'Salary': [500000, 1000000, 45000, 2500000, 52000000]}

df = pd.DataFrame(data)
print(df)


'''
-> The head() function helps look at a subset of the data. It allows us to retrieve 
the topmost five rows of the DataFrame. In this case, we specify 3 as the argument 
to head(), indicating that we want to retrieve the first three rows.

-> In the same way, we can look at the lowermost rows of the DataFrame 
using tail().
'''

print(df.head(3))

print(df.tail(2))

# look at the overall structure of the DataFrame, including the number of rows and columns it contains.
'''
-> The result is a tuple that contains two values. The first value represents the 
number of rows in the DataFrame, while the second value represents the number 
of columns. We got (5, 4) in the  output, which means that the DataFrame 
has 5 rows and 4 columns.
'''
print(df.shape)

# Check Column Names
print(df.columns)

# Checking Summary Statistics of the data:
print(df.describe())

'''
-> The Summary includes the following statistical measures of the numerical
columns in the data:


->    Count: The number of non-missing values in each column.
->    Mean: The average value of the data in each column.
->    Standard Deviation: A measure of the variability or dispersion of the data.
->    Minimum: The smallest value observed in each column.
->    25th Percentile: The value below which 25% of the data falls.
->    50th Percentile (Median): The value below which 50% of the data falls.
->    75th Percentile: The value below which 75% of the data falls.
->    Maximum: The largest value observed in each column.

'''

# How to look at the number of missing values in each column
print(df.isnull().sum())

'''
-> The df.isnull().sum() provides a concise summary of the count of missing values 
in each column of the DataFrame, assisting us in understanding the presence 
and extent of missing data in the dataset.
'''

# How to drop missing values.
df = df.dropna()

'''
-> df = df.dropna() creates a new DataFrame that excludes rows containing missing 
values, ensuring that the resulting DataFrame contains only complete and valid 
data for further analysis or processing.
'''

# How to look at the number of duplicates in each column.
print(df.duplicated())

# How to drop duplicates from the data
df = df.drop_duplicates

# How to select columns
df['Name'] # Select a single column
df[['Name', 'Age', 'City']] # Select multiple columns

'''
-> Selecting a single column using df[‘Column Name’] allows us to extract and work 
with the values of a specific attribute from the DataFrame. Selecting multiple 
columns using df[[‘Column1’, ‘Column2’]] allows us to extract and work with 
multiple attributes simultaneously, enabling a more comprehensive analysis and 
exploration of the data.
'''

# How to select rows by index and label:
df.loc[2] # Select a row by label.
df.iloc[3] # Select a row by index.

'''
-> By calling df.loc[2], we instruct to extract and display the row with the label or 
index value of 2. The result is a series or a one-dimensional labelled array that 
contains the values present in that particular row. And by calling df.iloc[3], we 
instruct to extract and display the row located at index position 3.
'''

# some examples of filtering rows
df[df['Age'] > 25] # Select rows where Age is greater than 25 (filter row based on a condition.)
df.query('City == "New Delhi"') # filter rows using a query syntax.

'''
-> By calling df[df[‘Age’] > 25], we instruct to extract and display the rows that meet 
the specified condition, which is that the ‘Age’ column value should be greater 
than 25. And by calling df.query(‘City == “New Delhi”‘), we instruct to filter the 
DataFrame based on the condition that the ‘City’ column value should be 
equal to “New Delhi”.
'''

#  example of sorting your DataFrame according to the values of a particular column.
# Sort the dataframe by the values in a specified column.
df.sort_values(by='Salary')

# By calling df.sort_values(by=’Salary’), we instruct to sort the DataFrame in 
# ascending order based on the values in the ‘Salary’ column.

# an example of creating new columns using existing columns

# Creating a new column using existing columns
df['Salary_Per_Year'] = df['Salary'] * 12

'''
-> By calling df[‘Salary_Per_Year’] = df[‘Salary’] * 12, we instruct to perform the 
calculation for each row in the ‘Salary’ column, multiplying the salary value by 12, 
and assign the result to the new column ‘Salary_Per_Year’.
'''

# Renaming Colums
df_renamed = df.rename(columns = {
    'Name': 'Full Name',
    'Age': 'Age (years)'
})

'''
-> By calling df.rename(columns={‘Name’: ‘Full Name’, ‘Age’: ‘Age (years)’}), we 
instruct to rename the ‘Name’ column to ‘Full Name’ and the ‘Age’ column to ‘Age (years)’.
'''

# How to convert a DataFrame to a CSV file
# Export the DataFrame to a CSV file
df.to_csv('data.csv', index = False)

# How to drop columns and rows
df_dropped_col = df.drop('Salary', axis = 1)
df_dropped_rows = df.drop([1,3], axis = 0)

'''
-> By calling df.drop(‘Salary’, axis=1), we instruct to drop the ‘Salary’ column from 
the DataFrame. And by calling df.drop([1, 3], axis=0), we instruct to drop the rows 
with index values 1 and 3 from the DataFrame.
'''

# How to merge and join DataFrames
data1 = {
    'key': ['A', 'B', 'C', 'D'],
    'value1': [1, 2, 3, 4]
}

data2 = {
    'key': ['B', 'C', 'D', 'E'],
    'value2': [5, 6, 7, 8]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Merging and Joining DataFrames
merged_df = pd.merge(df1, df2, on = 'key')
joined_df = df1.join(df2.set_index('key'), on = 'key')

'''
-> Merging DataFrames using pd.merge(df1, df2, on=’key’) combines two 
DataFrames into a single DataFrame based on a common key column. Joining 
DataFrames using df1.join(df2.set_index(‘key’), on=’key’) combines DataFrames 
based on a shared column by joining the columns of one DataFrame to another.
'''

# How to convert a column containing information about dates into a datetime data type:# Create a sample DataFrame with date and value columns

# Create a sample DataFrame with date and value columns

data = {
    'date': ['2023-07-01', '2023-07-02',
             '2023-07-03', '2023-07-04', '2023-07-05'],
    'value':[10, 15, 12, 8, 11]
}
df = pd.DataFrame(data)

# Convert the 'date' column to datetime data type
df['date'] = pd.to_datetime(df['date'])

'''
-> Converting a column to datetime data type using df[‘date’] = 
pd.to_datetime(df[‘date’]) ensures that the ‘date’ column is recognized as 
datetime data, enabling us to leverage time-based operations and 
analysis on the data.
'''

# How to aggregate and transform data

# Create a sample DataFrame
data = {'category': ['A', 'B', 'A', 'B', 'A'],
        'value1': [10, 15, 8, 12, 7],
        'value2': [5, 8, 4, 6, 3]}
df = pd.DataFrame(data)


# Advanced Aggregation
aggregated_df = df.groupby('category').agg({'value1': 'sum', 'value2': 'mean'})

# Advance Transformation
transformed_df = df.groupby('category').transform('mean')

# Display the original DataFrame, aggregated DataFrame, and transformed DataFrameprint("Original DataFrame:")
print(df)
print("\nAggregated DataFrame:")
print(aggregated_df)
print("\nTransformed DataFrame:")
print(transformed_df)

'''
-> Aggregation allows us to summarize and condense the data by computing 
summary statistics or combining multiple values into a single representation. 
In this case, we calculate the sum of ‘value1’ and the mean of ‘value2’ for each 
category, providing a consolidated view of the data grouped by categories. 
Transformation allows us to apply computations or modifications to individual 
values in the DataFrame based on group-specific properties. In this case, we 
transform the values in ‘value1’ and ‘value2’ to represent the mean value of their 
respective categories, providing a standardized representation of the data within 
each category.
'''


