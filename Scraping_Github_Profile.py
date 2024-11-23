# Web scraping is one of the most valuable skills every coder should have.

"""
# Scraping GitHub Profile using Python

When we open any GitHub account, we see a profile picture, the name of the user, 
and a short description of the user in the profile section. Here we will see how to 
scrape your GitHub profile image. For this task, you need some knowledge of HTML 
and the requests and BeautifulSoup libraries in Python.

If you have never used the BeautifulSoup library before, use the command 
mentioned below in your command prompt or terminal to install this library 
in your Python virtual environment:

    pip install beautifulsoup4

You don’t need to install the requests library as it is already present in the Python 
standard library.

"""

# import requests
# from bs4 import BeautifulSoup as bs

# github_profile = "https://github.com/amankharwal"
# req = requests.get(github_profile)
# scraper = bs(req.content, "html.parser")
# profile_picture = scraper.find("img", {"alt": "Avatar"})["src"]
# print(profile_picture)

"""
Now, if we click on the link we got as an output, we will see the profile picture of 
the GitHub user. This is how we can scrape profile images from any GitHub 
profile using Python.
"""

"""
Error Message:->
The error you're encountering, TypeError: 'NoneType' object is not subscriptable, 
happens because the scraper.find("img", {"alt": "Avatar"}) line is returning None, 
meaning it couldn't find an img tag with the alt attribute set to "Avatar" on the page.
"""


import requests
from bs4 import BeautifulSoup as bs

github_profile = "https://github.com/amankharwal"
req = requests.get(github_profile)
scraper = bs(req.content, "html.parser")

# Trying different selectors if the first one doesn't work
profile_picture_tag = scraper.find("img", {"alt": "Avatar"})

if profile_picture_tag is None:
    # Look for a different selector (for example, class name)
    profile_picture_tag = scraper.find("img", {"class": "avatar-user"})

if profile_picture_tag is not None:
    profile_picture = profile_picture_tag["src"]
    print(profile_picture)
else:
    print("Profile picture not found")

