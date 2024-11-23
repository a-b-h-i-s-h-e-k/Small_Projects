"""
The execution or running time of the program indicates how quickly the output is 
delivered based on the algorithm you used to solve the problem. To calculate the 
execution time of the program, we need to calculate the time taken by the program 
from its initiation to the final result.



It is important to calculate the execution time when working on a large project. 
When working on a large project, we have several approaches in mind. The best 
should be the one that takes the shortest execution time in all scenarios.


So to calculate the execution time of a Python program, we need to follow 
the steps mentioned below:

  1. First, store the time of initiation of the program into a variable;
  2. Write the Python program;
  3. Store the end time of the program into a variable;
  4. Subtract the time of initiation of the program from the end time of the program;
    
"""
# a simple program to create acronyms:

from time import time
start = time()

# python program to create acronyms
word = "Artificial Intelligence"
text = word.split()
a = " "
for i in text:
    a = a+str(i[0]).upper()
print(a)

end = time()
execution_time = end - start
print("Execution Time : ", execution_time)

"""
# Worst Case, Average Case, and Best Case
https://thecleverprogrammer.com/2020/11/09/worst-case-average-case-and-best-case/
"""
