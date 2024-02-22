#  A program that stores employee records
# Date: 21/02/2024
# Name : Lorna Waithira

e_name = input ("Enter employee name")
e_age = input (("Enter employee age")) 
e_salary = int(input (("Enter employee salary")))
e_bonuses =float (input (("Enter employee bonuses")))
percentage = (30/100)  
 
salary_inc = e_salary + (e_salary * percentage)

print ("The employee name is:", e_name )
print ("The employee age is:", e_age )
print ("The employee salary is:", e_salary )
print ("The employee bonuses is:", e_bonuses )
print ("The employee new salary is:", salary_inc )

bonus_ded = 5000
new_bonuses =  e_bonuses - bonus_ded


print ("The employee name is:", e_name )
print ("The employee age is:", e_age )
print ("The employee salary is:", e_salary )
print ("The employee new bonuses is:", new_bonuses)
print ("The employee new salary is:", salary_inc )
