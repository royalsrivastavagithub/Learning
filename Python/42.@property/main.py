"""
The @property decorator is used to implement a getter for a class property.
It is used to customize access to instance data.
It allows you to implement a getter without having to implement a setter.
"""
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.2f}cm"

    @property
    def height(self):
        return f"{self._height:.2f}cm"
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            raise ValueError("Width must be greater than 0")
    
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            raise ValueError("Height must be greater than 0")
        
    @width.deleter
    def width(self):
        del self._width
        print("Width deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height deleted")

rectangle1 = Rectangle(10, 20)

print(rectangle1.width)
print(rectangle1.height)

rectangle1.width = 23
rectangle1.height = 25

print(rectangle1.width)
print(rectangle1.height)

del rectangle1.width
del rectangle1.height
