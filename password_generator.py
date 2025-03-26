# Python Password Generator.


# Modules.
# Time module used for a more creative user experience.
# Secrets module used to ensure the most secure password combinations.
# Sys module used to exit the program in a controlled and precise fashion.

import time 
import secrets
import sys


# Function that prompts the user to start the program, error handler as well (try/except).
# Variable "password" for where the generator will be selecting the random characters from.
# Variables "chars" and "num" used to prompt the user with how many passwords and characters they want.

def generator():
    try:

        passwords = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"

        print("WELCOME TO THE PYTHON PASSWORD GENERATOR : ) \n")
        chars = int(input("Welcome to the password generator! How many characters would you like your password to be?: "))
        num = int(input("How many passwords would you like?: "))


        # Extra feature I added with the time module to make it more interesting.

        time.sleep(1.5)
        print("Configuring Password...\n")
        
        time.sleep(1)
        print("Creating a secure sequence....\n")
        
        time.sleep(1)
        print("Finalizing password.....\n")
        
        time.sleep(1)
        print("Password is ready!\n")
        time.sleep(0.5)
        
        # Tells the user the program is finished running.

        print("Done! Here is your password(s)! (Don't share this with anyone!!!)\n")


        # For loop that converts the input of the user into string format,
        # so it prints horizontally, which is more readable than vertically.
        # Another for loop is nested to randomly generate a secure combination of passwords.
        # Compliments of the secret module.

        for x in range(num):
            x = "\n"
            
            for y in range(chars):
                x += secrets.choice(passwords)
            
            print(x)

    
    # Error handler, if the user inputs a non-integer value, it will terminate the program.
    
    except ValueError:
        
        print("Sorry, invalid input, try again :/")
        sys.exit(1)

    
    # If statement making sure the user doesn't enter a negative number, sys.exit() is used to exit the program.
    
    if chars <= 0 or num <= 0:
        print("Please enter a number greater than 0!\n")
        sys.exit(1)


generator()


# Function used to prompt the user, gives them an option to restart the program, or quit.

def try_again():
    while True:

        repeat = input("\nWould you like to generate more passwords? (Y/N): ")
        
        if repeat.lower() == "y":
            generator()
            
        elif repeat.lower() == "n":
            print("Ok, Goodbye!")
            break
            
        else:
            print("Sorry, not Y or N, restart the program :/")
            break

try_again()






