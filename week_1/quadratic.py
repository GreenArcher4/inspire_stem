# quadratic equation
# Date: 20/02/2024
# Name : Lorna Waithira
import math

a = float(input ("Enter the coefficient of first term : "))
b = float(input("Enter the coefficient of second term : "))
c = float(input ("Enter the constant : "))

d = (b**2) - 4 * a * c
d_sqrt = math.sqrt (d)

x_1 = (-b + d_sqrt ) / 2 * a
x_2 = (+b - d_sqrt ) / 2 * a

print("The solution to of the quadratic equation is : ", x_1 )
print("The solution to of the quadratic equation is : ", x_2 )

