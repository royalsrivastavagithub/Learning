#for loop
print("1 to 10 :")
for i in range(1,10):
    print(i)


print("10 to 1")
for i in reversed(range(1,10)):
    print(i)    


numbers = [1,6,3,2,2,3,4,5]
for x in numbers:
    print(x)

print("1 to 10 were 5 will not be counted")

for i in range(1,10):

    if i == 5:
        continue
    else:
        print(i)

print("for loop will try to count to 10 but will  break at 7")

for i in range(1,10):
    if i == 7:
        break
    else:
        print(i)


        