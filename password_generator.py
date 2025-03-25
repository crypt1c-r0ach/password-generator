# Python Password Generator


# Modules

import time 
import secrets


# Function that prompts the user to start the program, error handler as well (try/except).
# Variable "password" for where the generator will be selecting the random characters from.
# Variables "chars" and "int" used to prompt the user with how many passwords and characters they want.

def generator():
    try:
        
        passwords = "1234567890!@#$%^&*()qwertyuiopasdfghjklzcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
        
        print("WELCOME TO THE PYTHON PASSWORD GENERATOR : ) \n")
        chars = int(input("Welcome to the password generator! How many characters would you like your password to be?: "))
        num = int(input("How many passwords would you like?: "))
        
        
        # Extra feature I added with the time module to make it more interesting.
        
        time.sleep(2)
        print("Configuring Password...\n")
        time.sleep(1.5)
        print("Creating a secure sequence....\n")
        time.sleep(1)
        print("Finalizing password.....\n")
        time.sleep(1)
    
    
        # Tells the user the program is finished running
        
        print("Done! Here is your password! (Don't share this with anyone!!!)\n")
        
        
        # For loop that converts the input of the user into string format,
        # so it prints horizontally, which is more readable than vertically.
        # Another for loop is nested to randomly generate a secure combination of passwords.
        # Compliments of the secret module.
        
        for x in range(num):
            x = "\n"
            for y in range(chars):
                x += secrets.choice(passwords)

            print(x)
    
    except ValueError:
        print("Sorry, invalid input, try again :/")
        

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


