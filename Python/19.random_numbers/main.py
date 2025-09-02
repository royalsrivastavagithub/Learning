import random


print(random.random())
print(random.randint(1,10))
print(random.randrange(1,10))
print(random.uniform(1,10))
print(random.choice([1,2,3,4,5,6,7,8,9,10]))
print(random.choices([1,2,3,4,5,6,7,8,9,10],k=3))
print(random.sample([1,2,3,4,5,6,7,8,9,10],k=3))

#dice
dice = [1,2,3,4,5,6]
print("DICE:",random.choice(dice))
#ROCK PAPER SCISSORS
print("ROCK PAPER SCISSORS:",random.choice(["ROCK","PAPER","SCISSORS"]))  