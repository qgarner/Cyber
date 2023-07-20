#Quinton Garner
#7/19/2023

# Today in Class we are building the childhood game Rock Paper Scissors
# We are going to import the random function for our code today
# Bonus objective can you put it on a while loop to play again
#Write your code below this line:

import random


while True:
    user_choice = input("Rock, Paper, or Scissors\n").lower()
    cpu_choice = ["rock" "paper" "scissors"]
    cpu_input = random.choice(cpu_choice)
    print(f"\nYou chose {user_choice}, computer chose {cpu_input}.\n")

    if user_choice == cpu_input:
        print("Both players chose {user_in} it is a tie")
    elif user_choice == "rock":
        if cpu_input == "paper":
            print("Paper covers rock you lose")
        else:
            print("Rock crushes scissors you win!")
    elif user_choice == "Scissors":
        if cpu_input == "Paper":
            print("Scissors cuts paper you win!")
        else:
            print("Paper covers rock you lose!")
    elif user_choice == "Rock":
        if cpu_input == "Scissors":
            print("Rock crushes scissors you win!")
        else:
            print("Paper covers rock you lose!")


play_again = input("Play again? Yes or no?")
if play_again.lower() != "yes":
        print("Game Over")