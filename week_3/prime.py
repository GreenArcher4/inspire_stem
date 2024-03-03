# A program to calculate prime numbers
# Date: 29/02/2024
# Name : Lorna 

lower= 1
upper= 99

print("\n")
print("--------The prime numbers are-------")
for number in range(lower, upper+1 ) :
  if number >1:
    for x in range(2,number):
       if (number % x)==0:
         break
    else:
      print(number)
      


#Single ;) suspected number
num= int(input("Enter the number suspected:"))
if num>1:
    for x in range(2,num):
       if (num % x)==0:
         print(num, "is not a prime number")
         break   
    else:
       print(num, "is a prime number")



def prime_nums():
   for x in range(2, 100+1):
    for y in range(2,x):
      if x % y==0 :
         break
   else:
     print(x)

print("The prime numbers between 1- 100 is :")
print(prime_nums)




       




