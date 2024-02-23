# Program that calculates pascals triangle
# Date: 22/02/2024
# Name : Lorna

from math import factorial 

col= int(input("Enter the number of columns in the pattern "))
print (" =====tha pattern is====") #indicates the beggining of the pattern

for i in range(0, col):
    for v in range (col -i +1):
      
      print ('')
    for v in range (0, i + 1):
          # representing pascals formula: nCr= n!/((n-r)!r!)
     print( factorial(i)//(factorial(v)* factorial(i-v)), end =  "   " )

print( )
