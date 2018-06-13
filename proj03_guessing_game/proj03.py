# Name:
# Date:
import random

print("Guessing Game!")
print("(type exit to end game)")
guess = input("Guess a number between 1 and 9: ")
random_number = random.randint(1,9)
amntguess = 0
while int(guess) != random_number and int(guess) != 0 or amntguess < 4:
    if int(guess) < random_number:
        print("That is too low!")
        amntguess = amntguess + 1
        guess = input("Guess a number between 1 and 9: ")
        if guess == "exit" or amntguess == 4:
            guess = 0
            print("The game has been Terminated.")
    elif int(guess) > random_number:
        print("That is too high!")
        amntguess = amntguess + 1
        guess = input("Guess a number between 1 and 9: ")
        if guess == "exit" or amntguess == 4:
            guess = 0
            print("The game has been Terminated.")
    else:
        amntguess = amntguess + 1
        print("You got it in " + str(amntguess) + " guesses!")
    #if  int(guess) > 9:
        #print("No don't do that.")
        #guess = 0




""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""
