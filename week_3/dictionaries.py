# 
# Date: 28/02/2024
# Name : Lorna 

laptop = {"make":"hp","color":"silver","weight":"1.5","year":"2021"}

print(laptop["make"])
print(laptop["color"])
print(laptop["year"])

#Edit
laptop["color"]= "red"
laptop["year"]= "2009"
laptop["size"]= "1200mm x 600mm" 
print(laptop)

#delete an element
del laptop["color"]
print(laptop)


siz_laptop = laptop.copy #doesnt work :(
print(siz_laptop)



for key,value in laptop.items:
  print("\n")
print(key)
print(value)
