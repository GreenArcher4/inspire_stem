# All about functions(user defined)(built in)
# Date: 29/02/2024
# Name : Lorna 

'''
block of code running together as a unit
Steps;
-initialise (uses a key word:def)
-Call the function
'''

#Define a function
def print_name():
    print("My name is Barca Waithan")

#Calling the function
print_name()

#details
def print_details(name,age,id,gender):
    print("I am {0}, {1}years old. My id no is {2} and my gender is {3}".format(name,age, id, gender))

print_details("Barca Waithan","19","090326","female")
print_details("Vincent ","21","309124","male")

#sum of numbers

def sum_nums(x,y):
   return  x+y

z = sum_nums(10,20)
print(z)

def prod_nums(x,y):
    return x*y

print(prod_nums(5,79))

def print_odds( first_no, second_no):
    for x in range( first_no, second_no):
        print ()
print_odds(1,15)

