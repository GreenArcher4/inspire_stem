# Program that calculates factorials of numbers
# Date: 22/02/2024
# Name : Lorna

import math

n = int(input("Enter the number whose factorial u want to find : "))

print ("The factorial is :", math.factorial (n)) # This is a built in function um python for finding factorial of number n

# Using for loop

factorial =  1
n =  int (input("Enter the n : "))

for i in range (1, n+1):
 factorial = factorial * i
 print ('The factorial is :', factorial)        

