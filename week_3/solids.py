# program calculating s.a and vol
# Date: 29/02/2024
# Name : Lorna 

#SPHERE
#Volume
def volume_sphere():
   radius= float(input("Enter radius"))
   pi =  3.14
   vol = pi* 4/3 * radius**3
   print("volume of sphere is:",vol)
  
volume_sphere()

#Surface Area
def sa_sphere():
   radius= float(input("Enter radius"))
   pi =  3.14
   s_a = pi* 4 * radius**2
   print("s.a of sphere is:",s_a)
  
sa_sphere()

#CYLINDER
#S.A
def sa_cylinder():
   radius= float(input("Enter radius"))
   height= float(input("Enter height"))
   pi =  3.14
   s_a = 2 *((pi* radius * height)+(radius**2* pi))
   print("s.a of cylinder is:",s_a)
  
sa_cylinder()

#Volume
def vol_cylinder():
   radius= float(input("Enter radius"))
   height= float(input("Enter height"))
   pi =  3.14
   vol = pi* radius**2 *height
   print("volume of cylinder is:",vol)

vol_cylinder()


#CUBE
#Sa
def sa_cube():
   base= float(input("Enter the base"))
   height= float(input("Enter height"))
   width =float(input("Enter width"))
   s_a = base* width *height
   print("sa of cube is:",s_a)

sa_cube()

#Volume
def vol_cube():
   length= float(input("Enter the length"))
   vol = length**3
   print("sa of cube is:",vol)

vol_cube()


#CONE
#S.A
def sa_cone():
  radius= float(input("Enter radius"))
  height= float(input("Enter height"))
  pi =  3.14
  s_a = (pi* radius**2 *height)/3
   
  print("volume of cylinder is:",s_a)

sa_cone()









"""
r = float(input(" Enter the value of the radius"))
h = float(input(" Enter the value of the height"))
r_sq = (r ** 2)

v =(pi * r_sq * h)
sa = ((2* pi* r * h)+ (2 * pi * r_sq ))

print(" The volume of the cylinder is :", v)
print(" The surface area of the cylinder is :", sa)
"""