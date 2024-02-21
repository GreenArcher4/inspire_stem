#This is AP and GP program
# Date: 20/02/2024
# Name : Lorna Waithira


# Arithmetic progression

a = float(input(" Enter the first term"))
d = float(input(" Enter the common difference"))
n = float(input(" Enter the number of terms"))

n_term =(a + d * (n - 1)) 
print("The nth term of the sequence is:", n_term)


# Geometric progression

a = float(input(" Enter the first term"))
r = float(input(" Enter the common ratio"))
n = float(input(" Enter the number of terms"))

n_term =(a * r**(n-1))
print("The nth term of the sequence is:", n_term)
