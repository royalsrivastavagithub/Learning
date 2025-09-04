import threading 
import time
def walk_dog():
    time.sleep(1)
    print("You finished walking the dog")

def walk_cat(name , age = 5):
    time.sleep(3)
    print(f"You finished walking {name} the cat of age {age}")

print("This will take 4 seconds")
walk_cat("millu")
walk_dog()

time.sleep(1)
print("This will take 3 second")
t2 = threading.Thread(target=walk_cat ,args = ("millu", 5))
t1 = threading.Thread(target=walk_dog)

t1.start()
t2.start()
t1.join()
t2.join()

print("Done") 