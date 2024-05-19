name = 'Ryan'
age = 38
print('Name:', name)
print('Age:', age)

number = 42
decimal = 3.14
text = 'Hello, Python!'
is_true = True

print ("Type of 'number':", type(number))
print ("Type of 'decimal':", type(decimal))
print ("Type of 'text':", type(text))
print ("Type of 'is_true':", type(is_true))

# Creating a list
fruits = ["apple", "banana", "orange"]

# Printing the entire list
print("Fruits:", fruits)

# Printing the first and last elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Adding a new fruit
fruits.append("grape")

# Removing a fruit
fruits.remove("banana")

# Printing the updated list
print("Updated fruits:", fruits)

# Creating a list of numbers
numbers = [1, 2, 3, 4, 5]

# Using a for loop to print each number
print("Using a for loop:")
for num in numbers:
    print(num)

# Using a while loop to print each number
print("Using a while loop:")
index = 0
while index < len(numbers):
    print(numbers[index])
    index += 1

# Using a for loop to calculate the total
total = 0
for num in numbers:
    total += num

# Printing the total
print("Total:", total)