'''
Lambda Functions
A lambda function is a small anonymous function.

lambda arguments : expression

A lambda function can take any number of arguments, but can only have one expression.

'''


def add(a,b):
    return a+b


print(add(5,7))


ad=lambda c,d:c+d
print(ad(7,5))


def add_and_multiply(a,b):
 return lambda c:((a+b)*c)


c=add_and_multiply(5,7)
print(c(5))


