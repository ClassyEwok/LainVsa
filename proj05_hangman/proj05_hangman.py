# Name:
# Date:


# proj05: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    wordlist = []
   # inFile = open(WORDLIST_FILENAME, 'r')
    for line in open('words.txt'):
        separator = " "
        line = line.split(separator)
        for value in line:
            wordlist.append(value)

    # line: string
    #line = inFile.readline()
    # wordlist: list of strings
    #wordlist = str.split(" ")
    #print (wordlist)
    print ("  " + str(len(wordlist)) + "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

word = choose_word(wordlist)
print(word)

# your code begins here!
amtletters = []
wordlist = []
amtguess = 6
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
wordansw = []
counter = 0
for letters in word:
    amtletters.append(letters)
print("Hello and welcome to Hang Man!")
print("Don't lose. The president's life is at stake!")
print("the word has " + str(len(amtletters)) + " letters in it.")
for value in amtletters:
    wordlist.append("_ ")
wordlist_clean = "".join(wordlist)
letterguess = input("Guess a letter: ")
while amtguess != 0 and len(wordansw) != len(amtletters):
    if letterguess in (alphabet):
        alphabet.remove(letterguess)
        clean_alphabet = "".join(alphabet)
        print("Letters left: " + clean_alphabet)
    wordlist_clean = "".join(wordlist)
    if letterguess in amtletters:
        print("You got a letter! ")
        counter = 0
        for letter in amtletters:
            if letterguess == letter:
                wordlist[counter] = letterguess
            counter = counter + 1
        print("It now is: " )
        print(" ".join(wordlist))
        letterguess = input("Guess another letter: ")
    else:
        print("Wrong letter!")
        amtguess = amtguess - 1
        print("Still just: " + wordlist_clean)
        letterguess = input("Guess another letter: ")
        
        counter = 0
        for letter in amtletters:
            if letterguess == letter:
                wordlist[counter] = letterguess
            counter = counter + 1
        print("It now is: " )
        print(" ".join(wordlist))
        letterguess = input("Guess another letter: ")
if amtletters == 0:
    print ("You failed. The president has died.")
elif amtletters == wordlist:
    print("You got the word!")
#elif
