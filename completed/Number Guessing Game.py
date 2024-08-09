import os # file , file direc , rename #2.
import random
import time

def clear_screen():
    os.system("cls")#windows cls

# Introduction
print("Hello, world!")
time.sleep(2)
clear_screen()

print("Welcome to the Number Guessing Game!")
time.sleep(2)
clear_screen()
print("I am going to guess a number between 1 and 100.")
time.sleep(2)
clear_screen()
print("You have to guess that number.")
time.sleep(2)
clear_screen()
print("If you guess the number correctly, you will win the game.")
time.sleep(2)
clear_screen()

# Game logic
number_to_guess = random.randint(1, 100) #1.
attempts = 0 #3.

def give_hint(guess, number):
    difference = abs(guess - number)
    
    if difference == 0:
        return "correct!"
    elif difference <= 2:
        return "extremely close!"
    elif difference <= 5:
        return "very close!"
    elif difference <= 10:
        return "close!"
    elif difference <= 20:
        return "somewhat close."
    elif difference <= 30:
        return "far."
    elif difference <= 50:
        return "very far."
    else:
        return "extremely far."

while True:
    try:
        user_guess = int(input("Enter your guess (1-100): "))
    except ValueError:
        print("please enter a valid number.")
        continue
    
    attempts += 1
    hint = give_hint(user_guess, number_to_guess)
    
    print(hint)
    
    if user_guess == number_to_guess:
        print(f"Congratulations Bro You guessed the number in {attempts} attempts.")
        break
