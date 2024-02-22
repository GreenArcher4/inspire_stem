# Program that checks if a string is a palindrome
# Date: 22/02/2024
# Name : Lorna 

word =  str(input("Enter the word"))
new_word = word[::-1]                # Shortcut that reverses the entire word
print("The reverse is", new_word)

if ( new_word == word):
    print(" This is a palindrome")
else :
    print(" This is a not palindrome")

