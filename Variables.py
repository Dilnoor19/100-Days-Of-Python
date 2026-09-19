# Variable Stores a value (python is dynamically typed, no need to declare a type)

# Basic variable assignment
age = 25
name = "Alice"
price = 99.99
is_python_fun = True

# Reassign different types
value = 100         # Integer
value = "Python"    # Now string
value = [1, 2, 3]   # Now list

# Type Conversion
num_str = str(42)    # "42"
str_num = int("123")  # 123
num_float = float(7) # 7.0

# String methods
name = "python"
upper_name = name.upper()  # "PYTHON"

# List methods
numbers = [1, 2, 3]
numbers.append(4)  # [1, 2, 3, 4]

# Dictionary methods
user = {"name": "Alice", "age": 30}
keys = user.keys()  # dict_keys(['name', 'age'])

# Assign multiple variables
x, y, z = 1, 2, 3

# Swap values
a, b = 10, 20
a, b = b, a  # a=20, b=10

# Common formatting with f-strings
name = "Bob"
age = 25
print(f"{name} is {age} years old")

# Centering a string
name = "Dilnoor"
print(f"{name:{'-'}^20}")


# Practise exercises
# 1> Basic variable usuage

name , age , my_height ,am_i_a_student = "Dilnoor singh", 19, 5.10, True
print(name , age , my_height ,am_i_a_student)
print(type(name))
print(type(age))
print(type(my_height))
print(type(am_i_a_student))


# 2> Type conversion

intoInt = int("123")
intoString = str(123)
float_to_int = int(12.34)
bool_to_string = str(True)

print(type(intoInt))
print(type(intoString))
print(type(float_to_int))
print(type(bool_to_string))

print(intoInt)
print(intoString)
print(float_to_int)
print(bool_to_string)

# 3> Variable Manipulation
first_variable = 20
second_variable = 30

add = first_variable + second_variable
sub = first_variable - second_variable
divide = first_variable // second_variable
multiply = first_variable * second_variable

print(add,sub,divide,multiply)
