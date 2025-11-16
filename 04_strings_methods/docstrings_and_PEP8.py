

#DocStrings are the string literals that appear after the defn of a function ,classes,modules or methods:


def square_of_number(n):
    '''Takes the number n and 
    returns the square'''

    sq=n*n
    return sq


print(square_of_number(5))

print(square_of_number.__doc__)