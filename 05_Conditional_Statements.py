# Basic conditional structure
temperature = 22

if temperature > 30:
    print("It's hot outside!")
elif temperature > 20:
    print("It's a nice day!")
else:
    print("It's cold outside!")


# Basic if statement
age = 18

if age >= 18:
    print("You are an adult.")
    print("You can vote.")

# If statement with multiple conditions (using logical operators)
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive.")

# If statement with a single line of code
if age > 65: print("Senior citizen discount applied.")

# Falsy values in Python
if False:     print("This won't print")
if None:      print("This won't print")
if 0:         print("This won't print")
if "":        print("This won't print")
if []:        print("This won't print")
if {}:        print("This won't print")
if set():     print("This won't print")

# Truthy values in Python
if True:      print("This will print")
if 42:        print("This will print")
if "hello":   print("This will print")
if [1, 2, 3]: print("This will print")
