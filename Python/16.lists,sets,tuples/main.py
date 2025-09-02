#list
print("list:")
fruits = ["apple","banana","mango","orange"]

print(f"1. {fruits[0]}")
print(f"2. {fruits[-1]}")
print(f"3. {fruits[1:3]}")
print(f"4. {fruits[1:]}")
print(f"5. {fruits[:3]}")
print(f"6. {fruits[-2:]}")
fruits.append("grapes")
print(f"7. {fruits}")
for fruit in fruits:
    print(fruit)

#sets
print("sets:")
fruits = {"apple","banana","mango","orange"}
print(f"1. {next(iter(fruits))}")
for fruit in fruits:
    print(fruit)
fruits.add("grapes")
print(f"2. {fruits}")
fruits.remove("grapes")
print(f"3. {fruits}")
print(f"4. {fruits.union({'kiwi','pineapple'})}")
print(f"5. {fruits.difference({'apple','banana'})}")
print(f"6. {fruits.issubset({'apple','banana','mango','orange'})}")
#tuple
print("tuple:")
fruits = ("apple","banana","mango","orange")

print(f"1. {fruits[0]}")
print(f"2. {fruits[-1]}")
print(f"3. {fruits[1:3]}")
print(f"4. {fruits[1:]}")
print(f"5. {fruits[:3]}")
print(f"6. {fruits[-2:]}")

