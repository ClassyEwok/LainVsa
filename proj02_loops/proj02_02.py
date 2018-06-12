# Name:
# Date:

# proj02_02: Fibonaci Sequence
amt = int(input("How many Fibonacci numbers would you like to make? "))
pren = 0
curn = 1
for number in range(0,amt):
    print(curn)
    nexn = pren + curn
    pren = curn
    curn = nexn
"""
Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci 
sequence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 
1, 1, 2, 3, 5, 8, 13...
"""

amount = int(input("How many powers of two? "))
two = 2
for number in range(0,amount):
    print (two)
    nextone = two * 2
    two = nextone

amnt = int(input("How many Fibonacci numbers would you like to make? "))
n = 0
prenu = 0
curnu = 1
while n < amnt:
    print(curnu)
    nexnu = prenu + curnu
    prenu = curnu
    curnu = nexnu
    n = n + 1

amtn = int(input("What number for divisors? "))

for divisor in range(1, amtn):
    if amtn%divisor == 0:
        print(str(divisor))










