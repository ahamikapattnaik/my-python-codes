# Create a greeting bot

import random

def greeting_bot():
    #user details
    full_name = input("Please enter your full name: ")
    email_id = input("Please enter your email id: ")

    #use split function to display only first name
    first_name = full_name.split()[0]

    #some welcome messages
    welcome_messages = [
        f"Hello {first_name}! Make sure to practice as many questions possible!",
        f"Welcome {first_name} to GitHub. Be as creative as you can in coding problems!",
        f"Hello {first_name}! Happy Coding!",
    ]

    #display a random message
    print(random.choice(welcome_messages))

greeting_bot()
