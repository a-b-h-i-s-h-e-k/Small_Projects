"""
A string is a sequence of characters enclosed in single or double-quotes. String 
inversion is one of the most common problems in computer science. Here we need 
to reverse the characters of a string.



There are many ways to reverse a string using Python. we can use any method 
that you find easy unless we are told to use a specific method.

You must have heard of the concept of slicing in Python. 
"""

def reverse_string(string):
    return string[::-1]

a = "reyalp tseb eht si oitirk"
print(reverse_string(a))

'''
The first character in the string has index 0, and the last character has index n-1, 
where n is the length of the string. The string slicing operator “::” reads all the 
characters of the string, and -1, in the end, reverses the order of the characters. 
This is how we can reverse a string.
'''