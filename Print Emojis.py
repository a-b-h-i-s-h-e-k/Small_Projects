# Emojis are used to express our emotions while writing a message or any piece of text.

"""
Smiling, thumbs up, and the heart emoji are some of the emojis we often use while 
texting our friends or colleagues. It’s possible to print any emoji using the Python 
programming language. To print emojis using Python, you need to install the emoji 
module in your Python virtual environment. You can easily install it by using the pip 
command on your terminal or command prompt as mentioned below:

   -> pip install emoji

The "emoji.emojize" method helps you write the description of any emoji inside “::” 
while writing a piece of text. Below are examples of descriptions of some of the 
popular emojis:

 1.   :thumbs_up:
 2.   :red_heart:
 3.   :smiling_face:

You can use the description of any emoji inside “::” to print the emoji using Python. 
You can find the description of all the emojis here.
[https://carpedm20.github.io/emoji/]

"""

import emoji
print(emoji.emojize("I love reading books:books:"))
print(emoji.emojize("Some people have a very sensitive heart:red_heart:, please be kind with them.:hibiscus:"))


# message = emoji.emojize(
#     "You're the star in my night :star:, the light of my life :sun_with_face:, and you make my heart skip a beat :heartbeat:. "
#     "I can't wait to see where this goes :heart_eyes: :sparkling_heart:"
# )

# print(message)
