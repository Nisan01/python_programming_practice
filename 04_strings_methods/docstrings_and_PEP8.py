

#DocStrings are the string literals that appear after the defn of a function ,classes,modules or methods:
#DocStrings should be right after the functions ....otherwise NONE


def square_of_number(n):
    '''Takes the number n and 
    returns the square'''

    sq=n*n
    return sq


print(square_of_number(5))

print(square_of_number.__doc__)

#python enhancement proposal
#PEP-8 is actually a document that describes or guides the way to write python codes best way