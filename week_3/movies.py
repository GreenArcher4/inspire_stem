# A program that sorts, reverses, pops and counts the list of movies in a list
# Date: 27/02/2024
# Name : Lorna 

movies = ["MCUz","red notice", "nimona", "Avengers", "Mission Impossible", "TMNT"]
print (movies)

#Remove last movie in list
movies. pop()
print('\n',movies)

#Sort movies in list
movies. sort()
print('\n',movies)

# Reverse order of characters acc to sort
movies. reverse()
print('\n',movies)

#Count the numbers of movies in the list

print('\n',len(movies))

#Count a movie in the list
m= movies.count("MCUz")
print('\n',m)