# Loop Practice
# Author: Ubial
# Date: 10 October 2023
import time;

# Create a list of groceries
groceries = ["hot wheels", "lego", "ice cream", "video games", "carrots"]

# Do something for each thing in the list
# Print it out in a pretty way
# e.g.
#     * hot wheels
#       ---
#     * lego
#       ---
#       etc.

# print(f"* {groceries[0]}")
# print(f"  ---")
# print(f"* {groceries[1]}")
# print(f"  ---")
# print(f"* {groceries[2]}")
# print(f"  ---")

for item in groceries:
    print(f"* {item}")
    print(f"  ---")

# Using the above method, create the thing below:
# *
# **
# ***
# ****
# *****
# ******

pyramid = ["*", "**", "***", "****", "*****", "******"]

for row in pyramid:
    print(row)


# new years bot

new_year = ["10", "9", "8", "7", "6", "5","4", "3", "2", "1", "Happy New Year!!@!" ]

for countdown in new_year:
    print(f" {countdown}")
    time.sleep(2)
