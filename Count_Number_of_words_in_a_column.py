"""
While working on a Data Science task, sometimes we have to deal with textual 
data. One of the problems beginners face while working on a textual dataset is 
counting the number of words in a piece of text.


Most data science professionals use the pandas library for data handling and 
preparation. The pandas library doesn’t have any method to count the number of 
words in a piece of text. One way to solve this problem is by finding the length of 
the text by splitting the complete text.

"""
import pandas as pd
data = pd.read_csv("articles.csv" , encoding = 'latin1')
print(data.head())


# The dataset has two columns Article and Title
data["Number of Words"] = data["Article"].apply(lambda n: len(n.split()))
print(data.head())

# So the dataset has three columns now, Article, Title and the Number of Words 
# that contains the number of words in the article column.

"""
The pandas library doesn’t have any method to count the number of words in a 
piece of text. One way to solve this problem is by finding the length of the text by 
splitting the complete text. So, this is how you can count the number of words in any 
column while working on a textual dataset. 
"""
