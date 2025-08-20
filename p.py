name = input("Enter your name: ")
print("Your name is", name)
notes = input("enter your notes please: ")
with open("file.txt", "w") as file:
    file.write("Name: " + name + "\n")
    file.write("Notes: " + notes + "\n")

with open("file.txt", "r") as file:
 print(file.read())