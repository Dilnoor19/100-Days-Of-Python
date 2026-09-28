# Basic for loop example
for i in range(5):
    print(i)  # Prints 0, 1, 2, 3, 4

# Basic while loop example
count = 0
while count < 5:
    print(count)  # Prints 0, 1, 2, 3, 4
    count += 1

'''The for loop in Python is designed to iterate over a sequence (like a list, tuple, dictionary, set, or string). This makes it perfect for processing collections of data.'''
# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterating over a string
for char in "Python":
    print(char)

# Iterating with range()
for i in range(5):  # 0 to 4
    print(i)

# Range with start and stop
for i in range(2, 6):  # 2 to 5
    print(i)

# Range with start, stop, and step
for i in range(1, 10, 2):  # 1, 3, 5, 7, 9
    print(i)
