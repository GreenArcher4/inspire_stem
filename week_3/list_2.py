# A program that slices a list, copies a list to another
# Date: 28/02/2024
# Name : Lorna 

friends =['Stan','mercy','Jane','Mjamaa','Puri']

for friend in friends:
    print(friend)

#To copy one list into another
enemies = friends[:]
print("\n")

print(enemies)

for enemy in enemies:
    print(enemy)


#To slice the list to get part of it
    
fruits =['lemon','orange','guava','apple','kiwi']     #prints 1st 3
print("\n",fruits[0:3])

del fruits[0]

print("\n",fruits)

squares=[]   #initialises an empty list

for x in range (0,11):
    squares.append(x**2)

print(squares)

