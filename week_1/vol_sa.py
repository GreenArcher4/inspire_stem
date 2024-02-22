# Date: 20/02/2024
# Name : Lorna Waithira
#volume and surface area of cylinder and sphere

import math

#cylinder

pi =  3.14
r = float(input(" Enter the value of the radius"))
h = float(input(" Enter the value of the height"))
r_sq = (r ** 2)

v =(pi * r_sq * h)
sa = ((2* pi* r * h)+ (2 * pi * r_sq ))

print(" The volume of the cylinder is :", v)
print(" The surface area of the cylinder is :", sa)


# sphere
pi =  3.14
r = float(input(" Enter the value of the radius"))
h = float(input(" Enter the value of the height"))
r_cu = (r ** 3)

vs = (4/3 * r_cu * pi)
sas = (4 * pi * r_sq)

print(" The volume of the sphere is", vs)
print(" The surface area of the sphere is", sas)



