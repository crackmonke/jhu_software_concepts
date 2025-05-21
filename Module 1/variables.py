word = "python"
number = 42
coefficient = 2.87
fruit = ["apple", "mango", "grape"]
ordinal = {1: "first", 2: "second", 3: "third"}

type(word)
#<class 'str'>

print(2 * 3.1416 * 10)
#OR
pi = 3.1416
radius = 10
print(2 * pi * radius)

#Object Counters
str_counter = 0
for item in ("Alice", 30, "Programmer", None, True, "Department C"):
    if isinstance(item, str):
        str_counter += 1

print("Number of strings:", str_counter)

#Accumulators
numbers = [1, 2, 3, 4, 5]
sum_numbers = 0

for number in numbers:
    sum_numbers += number
print("Sum of numbers:", sum_numbers)

#Calculating the average
print("Average of numbers:", sum_numbers / len(numbers))

#temp variables
a = 5
b = 10

temp = a
a = b
b = temp

print("a:", a)
print("b:", b)

#Boolean variables
toggle = True

for _ in range(5):
    if toggle:
        print("Toggle is ON")
    else:
        print("Toggle is OFF")
    toggle = not toggle

def greet(name, verbose=False):
    if verbose:
        return f"Hello, {name}! Welcome to our platform."
    else:
        return f"Hello, {name}!"

print(greet("Alice", verbose=True))

#Data Storage Variables
contacts = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"}
]

for contact in contacts:
    print(contact)

for name, age, city in contacts:
    print(f"Name: {name}, Age: {age}, City: {city}")