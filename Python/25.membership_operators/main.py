word = "APPLE"

letter = input("Enter a letter: ")

if letter in word:
    print(f"{letter} is in {word}")
else:
    print(f"{letter} is not in {word}")

