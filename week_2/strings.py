# Strings in python
# Date: 22/02/2024
# Name : Lorna 

city = "nairobi "

 #first character n 
print (city[0])                  
print (city[1])                  
print (city[2])                  
print (city[3])                 
print (city[4])                   
print (city[5])
print (city[6]) #last character i

print('') # reverse

print (city[-1])                   
print (city[-2])                  
print (city[-3])                 
print (city[-4])                   
print (city[-5])
print (city[-6])
print (city[0]) 

print('')

#prints you a new (double)line <skips lines>
print (city)
print("\n") 

#upper case
print (city)
print (city.upper ())

print ('')

# converts to lover case
name ="LORNA"
print (name)
print (name.lower() ) 

#strip off whitespaces
town = "         Kileleshwa              "
print (town)
print (town.strip())

#new tab
print ("\t") 


# add two strings

f_name = "Jason"
s_name = "Todd"

full_name = f_name +'\t'+ s_name

print(full_name)

#Replace a character in a string
fruit = "orange"

print(fruit.replace('o','Y'))

#splitting a string
subject = "Physical : sciences"

print(subject.split(':'))
print(subject)

#print a numeric character in string
age = 30
height = 1.72

print("I am {1} years old and {0} meters tall".format(age,height))





