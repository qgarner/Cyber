#Quinton Garner
#7/17/2023

# Your challenge tonight is to write a basic adventure game using some of the  
#code provide below and using if/elif statments

yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]
 
# Introduction
name = input("What is your name, adventurer?\n")
print("Greetings, " + name + ". Let us go on a quest!")
print("You find yourself on the edge of a dark forest.")
print("Can you find your way through?\n")
 
# Start of game
response = ""
while response not in yes_no:
    response = input("Would you like to step into the forest?\nyes/no\n")
    if response == "yes":
        print("You head into the forest. You hear crows cawwing in the distance.\n")
    elif response == "no":
        print("You are not ready for this quest. Goodbye, " + name + ".")
        quit()
    else: 
        print("I didn't understand that.\n")
 
# Next part of game
response = ""
# Use if else statment from here to take you on a journey and have fun with it
while response not in directions:
    response = input("Which direction would you like to go\n left, right, forward, or backward\n ")
    if response == "left":
        print("You are going to the cabin. \n")
    elif response == "right":
        print("You are going to the oak tree.\n")
    elif response == "forward":
        answer = input("Do you want to go to the dark?\n yes/no\n")
        if answer == "yes":
                print("Don't get scared!")
        else:
            print("Your to scared you can go home!")
    else:
        print("You are going home!")

answer = input("Would you like to keep going?\n yes/no\n")
if answer == "yes":
    print("We will keep going")
else:
    print("You are so scared! Go home!")
