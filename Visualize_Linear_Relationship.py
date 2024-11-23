"""
A linear relationship is a statistical term that is nothing but the relationship 
between two variables. A linear relationship shows how well two variables x and y 
are related to each other. As a data science professional, we should know how to 
visualize a linear relationship as it will show the relationship between two numerical 
features of a dataset.



When the value of variable increases or decreases with the increase or decrease in 
the value of another variable, then it is nothing but a linear relationship. When we 
visualize a linear relationship, it shows whether the relationship between the two 
features is linear or not.

we can use any data visualization library in Python to visualize a linear 
relationship. I prefer to use plotly as it provides interactive results. But as so many 
Python programmers use matplotlib for data visualization, I will show you how to 
visualize a linear relationship with Python using plotly and matplotlib.

    # pip install statsmodels

"""


import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/Instagram.csv", 
                   encoding = 'latin1')

data = data.dropna()
print(data.head())

# Here’s how to visualize linear relationships by using the plotly library in Python:

figure = px.scatter(data_frame = data,
                    x = "Impressions",
                    y = "Likes",
                    size = "Likes",
                    trendline = "ols",
                    title = "Relationship between likes and Impressions")

figure.show()

"""
To visualize linear relationships using matplotlib, we have to 
use seaborn.regplot method. So here’s how to plot linear relationships by using 
the matplotlib library in Python:
"""

plt.figure(figsize = (10,8))
plt.style.use('fivethirtyeight')
plt.title("Relationship Bewtween Likes & Impressions")
sns.regplot(x = "Impressions", y = "Likes", data = data)
plt.show()
