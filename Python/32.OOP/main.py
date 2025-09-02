from car import Car

car1 = Car("Toyota",2018,"red",True)
car2 = Car("Honda",2019,"blue",False)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)
car1.describe()
car1.drive()
print("----------")
print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)  
car2.stop()  
car2.describe()