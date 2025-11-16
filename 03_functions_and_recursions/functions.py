
#Functions in Python


#A function is a block of code you can reuse

# Simple function
def greet(name):
    """Prints a greeting"""
    print("Hello,", name)

greet("Alice")  # Call function

# Function with return value
def add(a, b):
    """Returns sum of a and b"""
    return a + b

result = add(5, 3)
print("5 + 3 =", result)

# Function with default argument
def power(x, y=2):
    """Returns x raised to y (default square)"""
    return x ** y

print("3 squared:", power(3))
print("2^4:", power(2,4))

# Function with multiple returns
def stats(lst):
    """Returns min, max, sum of a list"""
    return min(lst), max(lst), sum(lst)

mn, mx, total = stats([1,2,3,4])
print("min:", mn, "max:", mx, "sum:", total)

# Lambda (anonymous) function
square = lambda n: n**2
print("5 squared:", square(5))
