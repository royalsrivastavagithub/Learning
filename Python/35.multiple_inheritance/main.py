class Animal:
    def eat(self):
        print("The animal is eating")

class Prey(Animal):
    def flee(self):
        print("The prey is fleeing")

class Predator(Animal):
    def hunt(self):
        print("The predator is hunting")

class Rabbit(Prey):
    def run(self):
        print("The rabbit is running")

class Hawk(Predator):
    def soar(self):
        print("The hawk is soaring")

class Fish(Prey, Predator):#multiple inheritance
    def swim(self):
        print("The penguin is swimming")


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()
fish.eat()
