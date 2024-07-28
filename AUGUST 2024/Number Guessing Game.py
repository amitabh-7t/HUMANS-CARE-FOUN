import os
import random
import time

print("hello world")
time.sleep(2)
os.system("cls")
print("welcome to number guessing game")
time.sleep(2)
os.system("cls")
print("i am going to guess a number between 1 to 100")
time.sleep(2)
os.system("cls")
print("you have to guess that number")
time.sleep(2)
os.system("cls")#clear screen
print("if you guess the number correctly then you will win the game")

# Game logic
number_to_guess = random.randint(1, 100)
attempts = 0

while True:
    user_guess = int(input("Enter your guess (1-100): "))
    attempts += 1
    
    if user_guess < number_to_guess:
        print("Too low! Try again.")
    elif user_guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
