# Mean, Median and Mode are the fundamentals of statistics used in almost every domain 
# where we deal with numbers. Python is one of the best programming languages for 
# numerical calculations. So we should know how to calculate mean, median and mode 
# using Python without using any built-in Python library or module.

# MEAN:-->
""" The mean is the average value of all the values in a dataset. To calculate the mean value 
of a dataset, we first need to find the sum of all the values and then divide the sum of all 
the values by the total number of values."""

list1 = [12, 16, 20, 12, 58, 75, 52, 43, 83,99]
mean = sum(list1)/len(list1)
print(mean)

# MEDIAN:-->
"""The Median is the middle value among all the values in sorted order. Here we need to 
calculate the mid-value of all the values in a dataset. But before calculating the Median, we 
need to arrange all the values in sorted order. There are two different ways of 
calculating the median value:
1. when the total number of values is even: Median  = [(n/2)th term + {(n/2)+1}th]/2
2. when the total number of values is odd: Median = {(n+1)/2}thterm
"""

list1 = [12, 16, 20, 12, 58, 75, 52, 43, 83,99]
list1.sort()

if len(list1) % 2 == 0:
    m1 = list1[len(list1) // 2]
    m2 = list1[len(list1) // 2 - 1]
    median = (m1 + m2) / 2
else:
    median = list1[len(list1) // 2]
    
print(median)



# MODE:-->
"""Mode is the most frequently occurring value among all the values."""

list1 = [12, 16, 20, 12, 58, 75, 52, 43, 83,99]
frequency = {}
for i in list1:
    frequency.setdefault(i, 0)
    frequency[i] += 1
    

frequent = max(frequency.values())
for i, j in frequency.items():
    if j == frequent:
        mode = i
print(mode)

