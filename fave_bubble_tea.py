# Bubble Tea Popularity Algorithm
# Author: Alan
# Date: 27 October 2023

# Ask 5 users what their favourite bubble tea place is
# Prints out a summary of the data

# ------ CONSTANTS

NUM_RESPONDENTS = 7

# ------

# Like counters
coco_likes = 0      # Initialize the variable to 0
suntea_likes = 0
chatime_likes = 0
bubqueen_likes = 0
other_likes = 0

for _ in range(NUM_RESPONDENTS):
    # Ask the user what their favourite place is
    print("What's your favourite bubble tea place?")
    fave_place = input().strip(",.?! ").lower()

    # Tally or counting algo
    if fave_place == "coco":
        coco_likes = coco_likes + 1
    elif fave_place == "suntea":
        suntea_likes += 1       # alternate to above
    elif fave_place == "chatime":
        chatime_likes += 1
    elif fave_place == "bubble queen":
        bubqueen_likes += 1
    else:
        other_likes += 1

coco_persentage = round((coco_likes / NUM_RESPONDENTS) * 100, 2)
suntea_persentage = round((suntea_likes / NUM_RESPONDENTS) * 100, 2)
chatime_persentage = round((chatime_likes / NUM_RESPONDENTS) * 100, 2)
bubqueen_persentage = round((bubqueen_likes/ NUM_RESPONDENTS) * 100, 2)
other_persentage = round((other_likes/ NUM_RESPONDENTS) * 100, 2)

# Print out a summary
print(f"CoCo Likes: {coco_likes} ")
print(f"CoCo Percentage: {coco_persentage}%")
print(f"Sun Tea Likes: {suntea_likes}")
print(f"Sun Tea Percentage: {suntea_persentage}%")
print(f"Chatime Likes: {chatime_likes}")
print(f"Chatime Percentage: {chatime_persentage}%")
print(f"Bubble Queen Likes: {bubqueen_likes}")
print(f"Bubble Queen Percentage: {bubqueen_persentage}%")
print(f"Other Location Likes: {other_likes}")
print(f"Other Location Percentage: {other_persentage}%")
