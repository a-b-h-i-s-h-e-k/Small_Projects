"""

## Password Authentication is the process of checking the identity of a user. Almost every 
online platform today makes sure that they only give access to the real user which can be 
only possible by asking for a password while a user wants to log in to the account.



Q. What is a Password Authentication System?

A password authentication system is a system that is used for the identification of a user. 
Think of it like a login screen that you see while logging in to your Facebook account. 
It asks for your email or a username and then it asks for your password. If you have 
entered the correct password then it verifies you as the real user.

Creating a logic-based password authentication system is also a popular question in the 
coding interviews.


To create a password authentication system using Python we have to follow the steps:

1. Create a dictionary of usernames with their passwords.
2. Then you have to ask for user input as the username by using the input function 
in Python.
3. Then we have to use the getpass module in Python to ask for user input as the 
password. Here we are using the getpass module instead of the input function to 
make sure that the user doesn’t get to see what he/she write in the password field.

The getpass module is used to securely handle password input, meaning the password 
will not be displayed on the screen when typed.

"""

import getpass

# 1. Database Initialization
"""
    The database variable is a dictionary that stores usernames as keys and corresponding passwords 
    as values.
"""

database = {"luck.singh": "557842er3", "range.rover": "2546hu67@4l",
            "bhupendar.jogi": "2154sw#g6", "tharabhai.jogendar": "151sd1534g@f4",
            "ella.elf": "25ws34#f@g%tha"}

# 2. User Input
"""
-> The input() function prompts the user to enter their username.
-> The getpass.getpass() function prompts the user to enter their password, but the 
input is hidden for security purposes (it won't be visible as they type).
"""

username = input("Enter your Username : ")
password = getpass.getpass("Enter your Password : ")


# 3. Username and Password Validation Loop

"""
-> The code iterates over the keys (usernames) in the database dictionary using a for loop.
-> The if statement checks if the entered username matches any key in the dictionary.
-> If a match is found, it enters a while loop to check if the entered password matches the 
   stored password for that username (database.get(i) retrieves the password associated 
   with the username).
   
 -> If the password does not match, the user is prompted again to enter the password until it matches.
 -> Once the correct password is entered, the while loop is exited, and the program proceeds.
 """

for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Enter Your PASSWORD Again : ")
        break

# 4. Output
"""
After the 'while loop' exits (indicating the password is correct), the program prints "Verified", 
confirming that the user has successfully logged in.
"""    
print("Verified")
        