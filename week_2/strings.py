# Strings in python
# Date: 22/02/2024
# Name : Lorna 

city = "nairobi"

print (city[0]) # first character n
print (city[1])
print (city[2])
print (city[-1])
print (city[-2])
print (city[-3])
print (city[-4]) #last character i

#Convert to upper case

print (city)
print("\n\n") #prints you a new (double)line <skips lines>
print (city.upper ())

name ="LORNA"
print (name)
print (name.lower() ) # converts to lover case

town = "         Kileleshwa              "
print (town)
print ("\t") #new tab
print (town.strip())

# add two strings

f_name = "Jason"
s_name = "Todd"

full_name = f_name + s_name

print(full_name)

#Replace a character in a string
fruit = "orango"

print(fruit.replace('o','Y'))

#splitting a string
subject = "Physical:sciences"

print(subject.split(":"))

#print a numeric character in string
age = 30
height = 1.72

print("I am {0} years old and {1} meters tall".format(age,height))





