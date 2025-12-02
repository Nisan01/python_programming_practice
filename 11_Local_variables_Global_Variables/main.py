
#A local variable is a variable that is defined within a function and is only accessible within that function. 
# It is created when the function is called and is destroyed when the function returns.

#On the other hand, a global variable is a variable that is defined outside of a function
#  and is accessible from within any function in your code.

x = 10  # global variable

def my_function():
    global x, y
    x = 5  # changes the global x
    y = 6  # becomes a global variable because of the 'global' keyword

my_function()
print(x)  # prints 5
print(y)  # prints 6
