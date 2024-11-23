'''

SequenceMatcher is a class in Python available in the difflib module, which 
provides functions for comparing sequences in two different pieces of text. 
So whenever you want to compare two text files, you can explore the difflib 
module in Python.

[difflib module - https://docs.python.org/3/library/difflib.html]


The SequenceMatcher class is available in the difflib module in Python, which is 
available in the Python standard library. we do not have to install it before using it. 
There are many classes in the difflib module to compare texts. One of those classes 
is SequenceMatcher which calculates how well the sequence of two texts matches 
each other. In simple words, it finds similarities in the sequence of two different 
texts.

'''

from difflib import SequenceMatcher
text1 = "Kritio is the best player in virtual world games."
text2 = "Kritio is also the best athelete in real world games too."
sequenceScore = SequenceMatcher(None, text1, text2).ratio()
print(f"Both are {sequenceScore * 100} % similar")



'''

-> SequenceMatcher: This is a class from the difflib module in Python, which is used to compare sequences, 
such as strings. It can find similarities between two sequences.

-> None: The first argument to SequenceMatcher is usually a function to ignore certain characters 
(like whitespace), but passing None means no special function is used, and all characters 
are considered.

-> text1 and text2: These are the two text strings you want to compare.

-> .ratio(): This method of the SequenceMatcher object calculates a similarity ratio between 
text1 and text2. It returns a float value between 0 and 1, where 1 means the texts are 
identical, and 0 means they are completely different.

-> sequenceScore: This variable stores the similarity ratio. For example, if sequenceScore 
is 0.85, it means the texts are 85% similar.
==============================================================================================================

-> sequenceScore * 100: Since sequenceScore is a ratio (a value between 0 and 1), multiplying 
it by 100 converts it into a percentage. For example, if sequenceScore is 0.85, then 
sequenceScore * 100 would be 85.0.

-> print(f"Both are {sequenceScore * 100} % similar"): This prints the 
similarity percentage to the console.

'''