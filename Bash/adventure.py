# Setup
import random
from random import randint

yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]

# Intro
name = input("What is your name?\n")
location = input("Where are you from?\n")

print("Welcome, " + name + "!")
print("I hear " + location + " is looking for volunters for a space exploration mission.")

# Start
response = ""

while response not in yes_no:
    response = input("Do you think you have what it takes?\nyes/no\n")
    if response == "yes":
        print("Confidence... I like that!\n")
    elif response == "no":
        print("Come back when you've got some chest hair.\n")
        quit()
    else:
        print("Does not compute. Let's try that again, shall we?\n")

# Part 1: Fitness Test 
print("We first need to ensure you're mentally adept for such a strenuous undertaking.")

def generator():
    return randint(1,5)
def rand_guess():
    random_number = generator()
    guess_left = 3
    flag = 0

    while guess_left > 0:
        guess = int(input("You have 3 chances to correctly guess a number from 1 to 5\n"))
        
        if guess == random_number:
            flag = 1
            break

        else:
            print("Ooh, so close. Try again!")
        guess_left -= 1

    if flag == 1:
        return True
 
    else:
        return False
 
if __name__ == '__main__':
    if rand_guess() is True:
        print("Congratulations! You are ready to explore the depths of Uranus!")
    else :
        print("Sorry, looks like you didn't make the cut.")