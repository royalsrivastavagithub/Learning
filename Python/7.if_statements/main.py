user_age = int(input("Enter your age: "))



if user_age > 100:
    print("You are very old maan !")
elif user_age >=18:
    print("You are adult")
elif user_age == 0:
    print("You are not born!")
elif user_age < 0:
    print("Really ?")
    
else:
    print("You are minor")