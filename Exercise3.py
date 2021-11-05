# Guessing game! Pick a number randomly. While user does not guess the
#  number correctly give an instruction about the number and take
#   another guess from user.

import random

number = random.randint(1, 10)

user = int(input("Guess a number between 1 and 10: "))

while user != number:
    if user > number:
        print("Decrease the number")
    else:
        print("Increase the number")

    user = int(input("Guess a number between 1 and 10: "))

print("Congrats, you did correct")


