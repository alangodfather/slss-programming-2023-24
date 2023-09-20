# Chatbot
# Author: Alan
# Date: September 20, 2023

# Greet the user
print("Hello there! 🤖")
print("I'm a crude Chatbot, here to talk to you")

# Get the User's name and store it in a variable
user_name = input("So... What's your name? ")

# Respond to the user's name in afriendly way
print(f"It's good to meet you {user_name}.")

# Ask the user what their favourite food is
favourite_food = input("Hm.. What is your favourite food? ")

# Make a commnet about their food but NOT BE TERRIBY REPETATIVE

# Creata a list of possible responses
list_of_food_responses = [
    f"Oh I've never had {favourite_food} before. "
    "Hmmmmmmm. That sounds good!"
    "I heard that that is edelicious"
    "Cool."
    ]

# Choose one of those responses randomly
import random 
random_food_response = random.choice(list_of_food_responses)
# Print out that chosen response
print(random_food_response)