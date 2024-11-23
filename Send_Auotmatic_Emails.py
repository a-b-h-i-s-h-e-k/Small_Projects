""" 
Every time we register on a new app, you automatically recive a welcome message
with your name on it.


## How to Send Automatic Emails using Python?

To send automatic emails using Python, we must first understand how to send an email 
using the Python programming language. Once you know how to send an email using 
Python, the next thing you need to figure out is what you want to send automatically. For 
example, many companies send OTP or welcome messages, while some companies 
even send newsletters to newly registered users.

I will automatically send a welcome message to the newly registered user. For this task, 
we must first generate a google app password for your Gmail account.


-> It is very important to generate a Google app password for your Gmail account, as you will 
be sending automatic emails using Python through your Gmail account. 
Once you’ve generated your Google app password.

Google app password link -> https://support.google.com/accounts/answer/185833?hl=en

"""

import os
import random
import smtplib

def automatic_email():
    user = input("Enter Your Name >>: ")
    email = input("Enter Your Email >>: ")
    message = (f"Dear {user}, Welcome to TheCodeBeggining")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("Your Gmail Account", "Your App Password")
    s.sendmail('&&&&&&&&&&&', email, message)
    print("Email Sent!")
    
automatic_email()

"""
In the code above I have defined a Python function that will automatically send emails to a 
newly registered user. This function will start by asking for the user’s name and email. Then 
the user’s name will be stored in the message. Then in the 36th line of the code above, 
you need to replace the first parameter with your email and the second parameter 
with the google app password you generated before. After that just run the above code
and see output for yourself.
"""
"""
output:->
Enter Your Name >>: Tech something
Enter Your Email >>: tech.anything@gmail.com
Email Sent!
"""

