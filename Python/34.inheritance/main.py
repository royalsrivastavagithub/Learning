class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog (Animal):
    def bark(self):
        print(f"{self.name} is barking")

    def eat(self):
        print(f"{self.name} is eating chicken")


dog1 = Dog("Romy")
dog1.eat()
dog1.sleep()
dog1.bark()
print(dog1.is_alive)
print(dog1.name)

