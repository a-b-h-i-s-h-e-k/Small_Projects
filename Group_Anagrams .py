"""

Anagrams are words formed by rearranging the letters of another word, 
For example, car and arc, cat and act, etc. Grouping anagrams is one of the 
popular questions in coding interviews.

# Group Anagrams using Python

Grouping anagrams is one of the popular questions in coding interviews. Here you 
will be given a list of words, and you have to write an algorithm to group all the 
words which are anagrams of each other.

"""

from collections import defaultdict

def group_anagrams(a):
    dfdict = defaultdict(list)
    for i in a:
        sorted_i = "".join(sorted(i))
        dfdict[sorted_i].append(i)
    return dfdict.values()

# Now let’s test the function by creating a list of words containing anagrams and 
# some other words:

words = ["tea", "eat", "bat", "ate", "arc", "car"]
print(group_anagrams(words))

"""

# The function group_anagrams is designed to group words that are anagrams of each other. 
Here's a brief explanation of how it works:

1. Initialization: A defaultdict called dfdict is created where each key corresponds to a list. 
This allows us to easily group words together.

2. Loop Through Words: The function iterates over each word i in the input list a.

3. Sort Characters: For each word, it sorts the characters alphabetically to create a standardized 
form (e.g., "cat" becomes "act"). However, there is a small mistake here: the function uses 
" ".join(sorted(i)), which inserts spaces between the sorted characters. Instead, it should just 
be ''.join(sorted(i)).

4. Grouping Anagrams: The sorted word is used as a key in the dictionary dfdict. The original 
word is then appended to the list corresponding to this key. This way, all words that are 
anagrams of each other end up in the same list.

5. Return Values: Finally, the function returns the values of the dictionary, 
which are lists of anagrams.


# Example:
If a = ["cat", "tac", "act", "dog", "god"], 
the function will group them as 
[['cat', 'tac', 'act'], ['dog', 'god']].

"""