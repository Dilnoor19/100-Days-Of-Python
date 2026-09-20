text = "Python Programming"

# capitalize() - Converts first character to upper case
print(text.capitalize())    # "Python programming"

# casefold() - More aggressive lower() for case-insensitive matching
print(text.casefold())     # "python programming"

# lower() - Converts string to lower case
print(text.lower())        # "python programming"

# upper() - Converts string to upper case
print(text.upper())        # "PYTHON PROGRAMMING"

# swapcase() - Swaps cases of all characters
print(text.swapcase())     # "pYTHON pROGRAMMING"

# title() - Converts first character of each word to upper case
print(text.title())        # "Python Programming"



# Alignment and Padding Methods
text = "Python"

# center() - Returns centered string with specified width
print(text.center(10, '*'))    # "**Python**"

# ljust() - Left-aligns string with specified width
print(text.ljust(10, '-'))     # "Python----"

# rjust() - Right-aligns string with specified width
print(text.rjust(10, '-'))     # "----Python"

# zfill() - Fills string with zeros from left
print(text.zfill(8))           # "00Python"


# Search and Replace Methods
text = "Python Programming Python"

# count() - Returns number of occurrences of substring
print(text.count('Python'))    # 2

# find() - Returns lowest index of substring (-1 if not found)
print(text.find('Python'))     # 0

# rfind() - Returns highest index of substring (-1 if not found)
print(text.rfind('Python'))    # 18

# index() - Like find() but raises ValueError if not found
print(text.index('Python'))    # 0

# rindex() - Like rfind() but raises ValueError if not found
print(text.rindex('Python'))   # 18

# replace() - Replaces substring with another string
print(text.replace('Python', 'Java'))  # "Java Programming Java"

# Splitting and Joining Methods
# split() - Splits string at specified separator
text = "Python,Java,C++"
print(text.split(','))         # ['Python', 'Java', 'C++']

# rsplit() - Splits string from right
print(text.rsplit(',', 1))     # ['Python,Java', 'C++']

# splitlines() - Splits string at line boundaries
text = "Line 1\nLine 2"
print(text.splitlines())       # ['Line 1', 'Line 2']

# join() - Joins iterable elements with string as separator
words = ['Python', 'is', 'awesome']
print(' '.join(words))         # "Python is awesome"

# partition() - Returns tuple of three parts
text = "Python:Programming"
print(text.partition(':'))     # ('Python', ':', 'Programming')

# rpartition() - Like partition() but from right
print(text.rpartition(':'))    # ('Python', ':', 'Programming')

# String Stripping Methods
text = "   Python   "

# strip() - Removes leading and trailing whitespace
print(text.strip())            # "Python"

# lstrip() - Removes leading whitespace
print(text.lstrip())           # "Python   "

# rstrip() - Removes trailing whitespace
print(text.rstrip())           # "   Python"

