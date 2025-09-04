class Animal() :
    alive = True

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
    

class Car:
    alive = False
    def speak(self):
        return "Beep!"
        
animals  = [Dog(), Cat(), Car()]
for animal in animals:
    print("Speak: ",animal.speak())
    print("Alive: ",animal.alive)