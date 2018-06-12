# Name:
# Date:

# proj01: A Simple Program

# Part I:
# This program asks the user for his/her name and grade.
#Then, it prints out a sentence that says the number of years until they graduate.

name = input("What is your name? ")
name = name[0].upper() + name[1:]
grade = int(input("That is a cool name. What grade are you in? "))
years = str(13 - grade)
print (name + ", you will graduate in " + years + " years!")

# Part II:
# This program asks the user for his/her name and birth month.
# Then, it prints a sentence that says the number of days and months until their birthday
bmonth = int(input("What month were you born in, " + name + "? "))
bday = int(input("What day were you born on? "))
submonth1 = bmonth - 6
submonth2 = 6 - bmonth
submonth3 = bmonth - 6 - 1
subday1 = bday - 12
subday2 = 30 - (12 - bday)
if (bmonth >= 6) and (bday >= 12):
    print ("You have " + str(submonth1) + " month(s) ")
    print("and " + str(subday1) + " day(s) until your birthday!")
elif (bmonth >= 6) and (bday <= 12):
    print("You have " + str(submonth3) + " month(s) ")
    print("and " + str(subday2) + " day(s) until your birthday!")
elif (bmonth <= 6) and (bday <= 12):
    print ("You have " + str(submonth2) + " month(s) ")
    print("and " + str(subday1) + " day(s) until your birthday!")
else:
    print ("You have " + str(submonth3) + " month(s) ")
    print("and " + str(subday2) + " day(s) until your birthday!")
age = int(input(name + ", how old are you? "))
if age < 13:
    print("You can see G and PG movies.")
elif (age >= 13) and (age < 18):
    print("You can see G, PG, and PG-13 movies.")
elif age >= 18:
    print("Since you are " + str(age) + ", you can see any movie you want!")
animal = input("What is your favorite animal? ")
color = input("What is your favorite color, " + name + "? ")
food = input("What is your favorite food to consume? ")
sport = input(name + ", what is your favorite sport? ")
song = input("Finally, what is your favorite song to listen to? ")
print("Great! Here is a sentence that is made just for you: ")
print("A " + color + " " + animal + " named " + name + ", played " + sport + " while listening to " + song + " and eating " + food + "! ")

# If you complete extensions, describe your extensions here!
