from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self,radius):
        self.name = "Circle"
        self.radius = radius

    def area(self):
        return self.radius * self.radius

class Square(Shape):
    def __init__(self,side):
        self.name = "Square"
        self.side = side
    def area(self):
        return self.side * self.side


class Triangle(Shape):
    def __init__(self,base,height):
        self.name = "Triangle"
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2   

class Pizza(Circle):
    def __init__(self,topping,radius):
        super().__init__(radius)
        self.name = "Pizza"
        self.topping = topping
      


shapes = [Circle(4),Square(5),Triangle(6,7),Pizza("pepperoni",8)]


for shape in shapes:
    print(f"The area of the {shape.name} is {shape.area()}")