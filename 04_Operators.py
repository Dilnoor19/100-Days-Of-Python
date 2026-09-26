# Basic arithmetic
x = 10
y = 3

print(x + y)    # Addition: 13
print(x - y)    # Subtraction: 7
print(x * y)    # Multiplication: 30
print(x / y)    # Division: 3.3333... (returns float)
print(x // y)   # Floor division: 3 (returns integer)
print(x % y)    # Modulus: 1 (remainder)
print(x ** y)   # Exponentiation: 1000 (x raised to power y)

# Comparison operators
x = 10
y = 5

print(x == y)    # Equal to: False
print(x != y)    # Not equal to: True
print(x > y)     # Greater than: True
print(x < y)     # Less than: False
print(x >= y)    # Greater than or equal to: True
print(x <= y)    # Less than or equal to: False

# Chained comparisons
age = 25
print(18 <= age < 65)  # Check if age is between 18 and 65: True

# Basic assignment
x = 10

# Combined operators
x += 5      # Same as: x = x + 5, Now x is 15
x -= 3      # Same as: x = x - 3, Now x is 12
x *= 2      # Same as: x = x * 2, Now x is 24
x /= 6      # Same as: x = x / 6, Now x is 4.0 (note: becomes float)
x //= 2     # Same as: x = x // 2, Now x is 2.0
x **= 3     # Same as: x = x ** 3, Now x is 8.0
x %= 3      # Same as: x = x % 3, Now x is 2.0

# Works with strings too
message = "Hello"
message += " World"  # message becomes "Hello World"
