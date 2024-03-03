# this  is a class describing cars
# Date: 1/03/2024
# Name : Lorna 

class car:
    def __init__(self,model,make,year_of_production,fuel_capacity,color,horse_power):
        self.model= model
        self.make = make
        self.year_of_production = year_of_production 
        self.fuel_capacity= fuel_capacity
        self.color= color
        self.horse_power = horse_power

  
  
    def print_make(self,make) :
          print("The car is of  that {0} make" .format(self,make))


    def set_make(self,make):
      self.make = make

    def get_make(self):
      return self.make
    
    def set_color(self,color):
       self.color = color

my_car = car("Bugatti","Chiron", "2021","2400cc","midnight blue","3900hp")

friends_car = car("Tesla" ,"model s", "2020","2400cc","glacier blue","3900hp")

#my_car.print_make("Bugatti")

my_car.set_make("Bugatti")
friends_car.set_make("Tesla")

print(my_car.get_make())
print(friends_car.get_make())

    
my_car.set_color("red")
friends_car.set_color("grey")

"""
print(my_car.get_color())
print(friends_car.get_color())
"""




"""
Install
create a form with reg of students : name, age 
display the form
"""