# coding=utf-8
# Name:
# Date:

"""
proj04

practice with lists

"""

#Part I
#Take a list, say for example this one:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
empty_list = []

#if a[0:] < 5:
    #print()
#and write a program that prints out all the elements of the list that are less than 5.
lessnum = int(input("The following numbers are less than: "))
for x in range(len(a)):
    if a[x] < lessnum:
        print(a[x])


for x in range(len(a)):
    if a[x] < lessnum:
        empty_list.append(a[x])
print(empty_list)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for numa in a:
    if numa in a and numa not in c:
        c.append(numa)
for numb in b:
    if numb in b and numa not in c:
        c.append(numb)
if numa == numb:
    c.append(numb + numa)
print(c)








#Part II
# Take two lists, say for example these two:
b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that creates and prints a list that contains only the elements
# that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.





#Part III
# Take a list, say for example this one:

d = ["b", "a", "f", "y", "a", "t", "_", "p", "a", "R"]
e = []
asteric = "*"
# and write a program that replaces all “a” with “*”.
for letter in d:
    if letter == "a":
        e.append(asteric)
    else:
        e.append(letter)
print(e)



#Part IV
#Ask the user for a string, and print out whether this string is a palindrome or not.
palind = input("Enter a number to see if it's a palindrome: ")
list1 = []
for letter in palind:
    if letter != " ":
        list1.append(letter)
numletters = int(len(list1) / 2)
for value in range(numletters):
    if list1[0] == list1[-1]:
        list1 = list1[1:-1]
        if value == (numletters-1):
            print("This is a palindrome. ")
    else:
        print("Not a palindrome.")
