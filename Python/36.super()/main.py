class Shape:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"This is a {self.color} {self.is_filled}")

class Rectangle(Shape):
    def __init__(self,width,height,color,is_filled):
        super().__init__(color,is_filled)
        self.width = width
        self.height = height

class Square(Shape):
    def __init__(self,side,color,is_filled):
        super().__init__(color,is_filled)
        self.side = side

class Triangle(Shape):
    def __init__(self,base,height,color,is_filled):
        super().__init__(color,is_filled)
        self.base = base
        self.height = height

class  Circle(Shape):
    def __init__(self,radius,color,is_filled):
        super().__init__(color,is_filled)
        self.radius = radius

circle = Circle(5,"red",True)
print(circle.radius)
print(circle.color)
print(circle.is_filled)
circle.describe()
square = Square(5,"blue",True)
square.describe()