"""
Grouping elements of the same indices means grouping elements of two or more 
data structures according to their indices.


To group elements of the same index, you will initially have two or more lists inside 
a list like [[a, b], [c, d]]. To group the elements of these lists, you need to create two 
new lists where you will store the elements of both the lists at index 0[a, c] and 
index 1[b, d]. That is the meaning of grouping the elements of the same indices.

"""

inputLists = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
outputLists = []
index = 0

for i in range(len(inputLists[0])):
    outputLists.append([])
    for j in range(len(inputLists)):
        outputLists[index].append(inputLists[j][ index])
    index = index + 1
    
a, b, c = outputLists[0], outputLists[1], outputLists[2]
print(a,b,c)

"""

1. Initial Setup:
-> inputLists: This is a list of lists. Each sublist contains three numbers
-> outputLists: An empty list that will eventually hold the transposed lists.
-> index: Initialized to 0, this variable keeps track of the current index for 
the new lists that will be added to outputLists.

2. Outer Loop (for i in range(len(inputLists[0]))):
-> This loop iterates over the indices of the sublists in inputLists. len(inputLists[0]) 
gives 3, so i will take the values 0, 1, and 2.

3. Creating New Sublists:
-> For each value of i, a new empty list is appended to outputLists.
-> The inner loop (for j in range(len(inputLists))) iterates over the sublists in inputLists.
-> For each j, the code appends the element at position index in the j-th sublist to the 
index-th sublist in outputLists.

"""