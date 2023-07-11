#Quin Garner
#7/10/2023

# Create a Python script that performs the following:

# Prompt the user to type a string input as the variable for your destination URL.

# Prompt the user to select a HTTP Method of the following options:
# GET
# POST
# PUT
# DELETE
# HEAD
# PATCH
# OPTIONS
# Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.

# Using the requests library, perform a GET request against your lab web server.

# For the given header, translate the codes into plain terms that print to the screen; for example, a 404 error should print Site not found to the terminal instead of 404.

# For the given URL, print response header information to the screen.
from urllib import response
import requests
b = input("Get, Post, Put, Delete , Head, Patch, Options:")

if b == "Get":
    response = requests.get('https://www.google.com/')
elif b == "Post":
    response = requests.post('https://www.google.com/')
elif b == "Put":
    response = requests.put('https://www.google.com/')
elif b == "Delete":
    response = requests.delete('https://www.google.com/')
elif b == "Head":
    response = requests.head('https://www.google.com/')
elif b == "Patch":
    response = requests.patch('https://www.google.com/')
elif b == "Options":
    response = requests.options('https://www.google.com/')
else:
    print("input error")
    quit()

anwser = input("Enter yes or no: ")
if anwser == "yes":
    print(response)
else:
    print("cancelling")
