"""
Correcting spellings in a piece of text is one of the handy features that can be used 
in any application where users write content. For example, if you want to create a 
notepad, it should have a feature to identify and correct the wrong spellings. 



The SpellChecker module in Python is one of the handiest tools that can be used to 
correct misspelt words in a piece of text. If you have never used this Python module 
before, you can easily install it in your Python virtual environment by running the 
command mentioned below in your command prompt or terminal:

pip install pyspellchecker

"""


from spellchecker import SpellChecker
corrector = SpellChecker()

word = input("Enter a word : ")
if word in corrector:
    print("Correct")
else:
    correct_word = corrector.correction(word)
    print("Correct Spelling is ", correct_word)
    
"""
There are many alternatives in Python for the same task, but the spellchecker 
module is easy to use compared to other alternatives.
[textbob]
"""
