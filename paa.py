fruits = ["apple", "banana", "orange", "grapes", "pineapple"]
print("My fruits list:", fruits)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

fruits[1] = "Mango"
print("After changing second fruit:", fruits)

fruits.insert(2, "Watermelon")
print("After inserting Watermelon:", fruits)

user_fruit = input("Enter a fruit name to check: ")
print("Is it in the list?", user_fruit in fruits)

fruits.sort()
print("The new sorted array:", fruits)