# A program to calculate salary increment of an employee
# Date: 26/02/2024
# Name : Lorna 

name = str(input("Enter your name:"))
salary = int(input("Enter your salary:"))
print("\n")                                 #skip a line

if salary < 100000 :
 new_salary = salary *1.3
 print(name,",your new salary is:", new_salary,' enjoy ;)')

elif salary< 150000 :
 new_salary = salary *1.15
 print(name,",your new salary is:", new_salary , ' enjoy ;)')

else :
 salary>150000 
 new_salary = salary *1.05
 print(name,",your new salary is:", new_salary, ' enjoy ;)')