# Name:
# Date:

# proj02: sum
varier = int(input("Enter a number to add, put a zero when done: "))
varied = varier
while varier != 0:
    variet = int(input("Enter a number to add, put a zero when done: "))
    varied = varied + variet
    varier = variet
print("Sum is " + str(varied))
# Write a program that prompts the user to enter numbers, one per line,
# ending with a line containing 0, and keep a running sum of the numbers.
# Only print out the sum after all the numbers are entered
# (at least in your final version). Each time you read in a number,
# you can immediately use it for your sum,
# and then be done with the number just entered.
answ = "Y"
while answ == "Y":
    p1shot = input("Player1, rock, paper, or scissors? ")
    p2shot = input("Player2, rock, paper, or scissors? ")
    if p1shot == "rock" and p2shot == "paper":
        print("Player2 wins! ")
    elif p1shot == "rock" and p2shot == "scissors":
        print("Player1 wins! ")
    elif p1shot == "paper" and p2shot == "rock":
        print("Player1 wins! ")
    elif p1shot == "paper" and p2shot == "scissors":
        print("Player2 wins! ")
    elif p1shot == "scissors" and p2shot == "paper":
        print("Player1 wins! ")
    elif p1shot == "scissors" and p2shot == "rock":
        print("Player2 wins! ")
    else:
        print("It is a Tie! ")
    answ = input("Good Game! Would you like to play again? (Y/N)")

#p1shot = input("Player1, rock, paper, or scissors? ")
#p2shot = input("Player2, rock, paper, or scissors? ")
#if p1shot == "rock" and p2shot == "paper":
#    print("Player2 wins! ")
#elif p1shot == "rock" and p2shot == "scissors":
#    print("Player1 wins! ")
#elif p1shot == "paper" and p2shot == "rock":
#   print("Player1 wins! ")
#elif p1shot == "paper" and p2shot == "scissors":
#    print("Player2 wins! ")
#elif p1shot == "scissors" and p2shot == "paper":
#   print("Player1 wins! ")
#elif p1shot == "scissors" and p2shot == "rock":
#   print("Player2 wins! ")
#else:
#   print("It is a Tie! ")
#answ = input("Good Game! Would you like to play again? (Y/N)")

#Example:
# Enter a number to sum, or 0 to indicate you are finished: 4
# Enter a number to sum, or 0 to indicate you are finished: 5
# Enter a number to sum, or 0 to indicate you are finished: 2
# Enter a number to sum, or 0 to indicate you are finished: 10
# Enter a number to sum, or 0 to indicate you are finished: 0
#The sum of your numbers is: 21
