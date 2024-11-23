"""
Pandas is an amazing Python library for working with data. Some of the 
amazing features it provides for working with data are:

    1. Intelligent data alignment
    2. Integrated handling of missing data
    3. Flexible data reshaping
    4. Easy insertion and deletion of columns
    5. data aggregation and transformation
    6. Merging and joining of datasets
    7. Time series functionality
    8. Academic and Commercial usage
  

-> There are so many functions that Pandas provide for all the features mentioned 
above. Although you need to learn all the functions that it provides but there are 
some very important functions in Pandas that you need to use in almost every data 
science task.

# Reading a Dataset:

Pandas provide functions to read data in any format. Mostly, we use 
CSV format datasets in data science tasks  

https://raw.githubusercontent.com/amankharwal/Website-data/master/GOOG.csv
"""

import pandas as pd
data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/GOOG.csv")

"""
# Looking at the First Five Rows:

It’s not easy to look at every row of data, so to get a first look at the data, it’s best to 
look at the first five rows to get an idea of what kind of data you’re going to be 
working with. So here’s how to look at the first five rows of the dataset:
"""

print(data.head())

"""
# Checking Null Values:

Having missing values in a dataset affects the analysis of the data, so it is very 
important to remove missing values or fill them in. But before you move on to fill in 
or delete your data, you need to know how many missing values you have. 
So here’s how to find missing values in a dataset:
"""

print(data.isnull().sum())

"""
Fortunately, this dataset does not have any missing values. If your data has missing 
values and you want to delete them.
"""
data.dropna()

"""
# Filling Missing Values:

If you want to fill all the missing values in a dataset with a specific value such as 
0, 1, 100, or any other value.
"""

data.fillna(0)


"""
# Fill Missing Values in a Dataset

When working on a data science task, sometimes many missing values act as a 
hindrance while getting the correct information from a dataset. We can easily 
remove the missing values, but sometimes we need to fill these values depending 
on the quantity of the dataset.



# Why do We Need to Fill Missing Values in a Dataset?

Sometimes the dataset we use to solve a problem contains a lot of missing values 
that can adversely affect the performance of a machine learning model. A dataset 
with a lot of missing values can give us wrong information. So if we have missing 
values in a dataset, here are some strategies we can choose to deal with them:

    1. Removing the whole row which contains missing values
    2. Filling the missing values according to the other known values

The first strategy is to remove the entire row containing a missing value. This is not 
a bad idea, but it can only be considered when the data is very large. If removing 
missing values results in a data shortage, then this will not be an ideal dataset for 
any data science task. This is where the second strategy comes in, which is to fill in 
the missing values according to the other known values. This strategy can be 
considered in any type of dataset.

So this is why we need to fill the missing values in a dataset.


# Fill Missing Values in a Dataset using Python

-> The scikit-learn library in Python offers the SimpleImputer() class which can be 
used for filling the missing values based on:

    1. Mean of the known values
    2. Median of the known values
    3. Most frequent value among the known values

So let’s go through all these methods one by one for filling the missing values of a 
dataset. I will first create a very simple dataset with some missing values:

"""

# import numpy as np
# data1 = np.array([[10, np.nan, 8],
#                  [9, 8, np.nan],
#                  [7, 10, 9]])
# print(data1)

# Here is how we can use the Mean of the other known values for filling the missing values:

### Filling values with mean

# from sklearn.impute import SimpleImputer
# mean_values = SimpleImputer(strategy = 'mean')
# data2 = mean_values.fit_transform(data1)
# print(data2)


# Here is how you can use the Median of the other known values for filling 
# the missing values:

# Filling Values with median

# from sklearn.impute import SimpleImputer
# median_values = SimpleImputer(strategy = 'median')
# data3 = median_values.fit_transform(data1)
# print(data3)

# Here is how you can use the most frequent value among the other known values 
# for filling the missing values:

# Filling values with most frequent values

# from sklearn.impute import SimpleImputer
# most_frequent = SimpleImputer(strategy = 'most_frequent')
# data4 = most_frequent.fit_transform(data1)
# print(data4)


"""
# Summary

So this is how we can fill missing values in any kind of data 
while working on a data science task. Filling the missing values is very 
important as these values act as a hindrance while collecting the 
correct information from a dataset.
"""


"""
# Query Data:

To ask specific queries to your data, you can use the query() function in pandas, 
which allows you to query specific records from the dataset, just like SQL. 
Here’s how you can query your data:
"""
print(data.query("Close > 1500"))

# I am requesting all rows where the values in the Close column 
# are more than 500.

"""
# Sorting Values:

You can also sort your dataset using Pandas according to a particular column. 
For example, below is how you can sort your data in ascending order according 
to the values of the Close column in the dataset:
"""
print(data.sort_values(by="Close"))

# how you can sort values in descending order:

print(data.sort_values(by="Close", ascending=False))

"""
# Descriptive Statistics:
To get the descriptive statistical information about your data, Pandas provides 
the describe() function that returns:    
 1. the total of all the columns     
 2. mean value of all the columns    
 3. the standard deviation of all the columns    
 4. minimum and maximum values of all the columns    
 5. 1st, 2nd, and 3rd quartile of all the columns
 
Below is how you can use this function:

"""

print(data.describe())

"""
# Correlation:

You can also look for the correlation between all the columns in the data 
by using the corr() function as shown below:
"""

print(data.corr())

"""
Summary

Pandas is a very fast and efficient DataFrame object for working with data. 
It provides highly efficient functions, ranging from reading and writing data 
to manipulate and preparing data for any kind of data science task.
"""