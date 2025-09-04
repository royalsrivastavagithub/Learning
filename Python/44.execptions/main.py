

try:
    number = int(input("Enter a number: "))
    print(2/number)
except ValueError:
    print("Please enter a number")

except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always execute")
