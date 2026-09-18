# Creating your first variables
message = "Hello, Python!"
user_age = 25
price = 19.99
is_available = True

# Print them to see their values
print(message)       # Shows: Hello, Python!
print(user_age)      # Shows: 25
print(price)         # Shows: 19.99
print(is_available)  # Shows: True

'''How Variables Work in Python'''
# Python allocates memory to store your data
# The data is stored in that memory location
# The variable name becomes a reference to that memory location

'''Modifing Variable'''
# Creating a variable
name = "Alice"   # Python creates space in memory for "Alice"
                # and 'name' points to it

# Changing the value
name = "Bob"     # The old value "Alice" is released
                # 'name' now points to "Bob"

# Changing the type
name = 42        # Python allows this! The variable now holds a number
                # This is dynamic typing in action

'''Rules for Variable Names'''
# # Must start with a letter (a-z, A-Z) or underscore (_)
# Can contain letters, numbers, and underscores
# Cannot start with a number
# Cannot use Python keywords (like 'if', 'for', 'while')
# Case-sensitive (age, Age, and AGE are different variables)

# Strings
name = "Alice"
message = 'Hello, ' + name    # String concatenation
print(message)               # Output: Hello, Alice

# Numbers
age = 25                    # Integer
height = 1.75              # Float
complex_num = 3 + 4j       # Complex number

# Boolean
is_student = True
has_license = False

# Checking types
print(type(name))          # <class 'str'>
print(type(age))           # <class 'int'>
print(type(height))        # <class 'float'>
print(type(is_student))    # <class 'bool'>
