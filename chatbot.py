# Chatbot
# Author: Alan
# Date: September 20, 2023
import random
import time
# Greet the user
print("Hello there! 🤖")
time.sleep(1.5)
print("I'm a crude Chatbott, here to talk to you")
# Get the User's name and store it in a variable
user_name = input("So... What's your name? ")
time.sleep(1.5)
fave_food = input("What's your favourite food? ") 
# Respond to the user's name in afriendly way
print(f"It's good to meet you {user_name}.")

# Ask the user what their favourite food is
if fave_food == "sushi":
    print("Yum!")
    print("I think I love sushi!")
elif fave_food == "burgers" or fave_food == "Burgers":
    print("🍔")
    print("Burgers, I hear are delious!")
# Make a commnet about their food but NOT BE TERRIBY REPETATIVE

# Creata a list of possible responses
list_of_food_responses = [
    f"Oh I've never had {fave_food} before. ",
    "Hmmmmmmm. That sounds good!",
    "I heard that that is delicious",
    "Cool."
    ]

print(list_of_food_responses[-1])

# Choose one of those responses randomly
import random 
random_food_response = random.choice(list_of_food_responses)
# Print out that chosen response
print(random_food_response)