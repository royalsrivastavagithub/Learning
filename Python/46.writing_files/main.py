txt_data = "Hello World"

with open("./file.txt","w") as file:
    file.write(txt_data)
    print(f"{txt_data} written to file.txt")

with open("./file.txt","r") as file:
    print(file.read())

with open("./file.txt","a") as file:
    file.write("\nHello World")

with open("./file.txt","r") as file:
    print(file.read())