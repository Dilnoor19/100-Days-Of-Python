# Basic types
integer = 42            # int
floating = 3.14         # float
text = "Hello"          # str
boolean = True          # bool
nothing = None          # NoneType

# Collection types
numbers = [1, 2, 3]            # list
coordinates = (4, 5)           # tuple
person = {"name": "Alice"}      # dict
unique_numbers = {1, 2, 3}      # set

# Python supports three numeric types: integers, floating-point numbers, and complex numbers.
# Integer operations
print(10 + 3)   # 13
print(10 // 3)  # 3 (floor division)
print(2 ** 4)   # 16 (exponentiation)

# practise 
# 1> Type Identification
print(type(42)) #int
print(type(3.14)) #float
print(type(True)) #bool
print(type([1, 2])) #list
print(type({"name": "Alice"})) #dict
print(type({1, 2})) #set
print(type((5,))) #tuple

# 2> Type Conversion
string_to_int = int("123")
int_to_float = float(15)
list_to_tuple = tuple([1, 2, 3])
set_to_list = list({"a": 1, "b": 2})

print(set_to_list)
