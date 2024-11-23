"""
Finding the missing number in an array is a popular coding interview question. 
According to LeetCode, this question is popular in the interviews of companies like 
Amazon, Adobe, Microsoft, LinkedIn, and many more.


# Find Missing Number using Python

Finding the missing number in an array means finding the numbers missing from 
the array according to the range of values inside the array. Most of the time, the 
question you get based on this problem is like:

  - Given an array containing a range of numbers from 0 to n with a missing 
    number, find the missing number in the input array.

To find the missing number in an array, we need to iterate over the input array and 
store the numbers in another array that we didn’t find in the input array while 
iterating over it. 

"""


def findMissingNumbers(n):
    numbers = set(n)           # Converts the list `n` into a set called `numbers`
    length = len(n)            # Gets the length of the list `n`
    output = []                # Initializes an empty list `output` to store missing numbers
    for i in range(1, n[-1]):  # Loops from 1 to the last element in the list `n`
        if i not in numbers:   # Checks if `i` is not in the set `numbers`
            output.append(i)   # If `i` is not in the set, it's missing, so add it to `output`
    return output              # Returns the list of missing numbers

listOfNumbers = [1,2,3,5,6,7,8,9,10,11,13,14,16,20]
print(findMissingNumbers(listOfNumbers))
