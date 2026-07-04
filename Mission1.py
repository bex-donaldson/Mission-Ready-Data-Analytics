# Data Source for all code
Joses_Book =  {"Book_Name": "Counting Miracles", "Author": "Nicolas Spark", "Year": 2025}
print(Joses_Book["Book_Name"])

# Exercise 1 Create a tuple that contains three numbers and print the last number from the tuple.

birth_years = (2020, 2022, 2024)
print(birth_years[2])

# Exercise 2: Create two sets and perform a union and an intersection operation between them.
set_one = {1,2,3,4,5,6}
set_two = {6,7,8,9,10,11,12}

# Set Union
print(set_one | set_two)

# Set Intersection
print(set_one & set_two)

# Exercise 3: Create a dictionary for a book with keys title, author, and year, and print the value for the author key.
Bex_Book = {"title": "Twilight", "author": "Stephenie Meyer", "year": 2005}
print(Bex_Book["author"])

# Exercise 4 Create a list of your three favorite fruits and print the second fruit from the list.
my_fruits = ["Fejoa", "Gold Kiwifruit", "Passion Fruit"]

print(my_fruits[1])

# Exercise 5: Control Structures Write a program that asks for your age and prints whether you are eligible to vote (18 or older).
age = 22
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Exercise 6: Functions Create a function that takes two numbers and returns their difference. Call the function with different numbers and print the result.
def differnce(a, b):
    return a - b

print(differnce(12,5))

