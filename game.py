# game.py

import random

print("Welcome to Rock Paper Scissors! What is your name?")
name = input("")
print(name, ", nice to meet you, good luck!")
print("rock, paper, scissors, shoot!")

#Prompt user input

user_choice=input("Choose 'rock' or 'paper' or 'scissors': ")
if user_choice in ["rock","paper","scissors"]:
    print("user chose:") 
    print(user_choice)
else: 
    print("You choice is not valid.  Reminder- all letters must be lowercase!")
    print("Try again")
    exit()

#Computer Coice (At Random)

x = ["rock","paper","scissors"]
computer_choice=random.choice(x)
print("computer chose:")
print(computer_choice)

#Winner Determination

if user_choice == computer_choice: 
    print ("Draw")
elif user_choice == "rock" and computer_choice == "paper" or user_choice == "paper" and computer_choice == scissors or user_choice == "scissors" and computer_choice == "rock":
    print ("You lose")
elif user_choice == "rock" and computer_choice == "scissors" or user_choice == "paper" and computer_choice == "rock" or user_choice == "scissors" and computer_choice == "paper":
    print ("You win")

print("Thanks for playing.  Have a nice day!")