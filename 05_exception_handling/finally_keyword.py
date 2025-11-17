

'''


finally is a block in Python that always runs, no matter what happens—
even if there is an error, a break, return, or continue.


'''

try:
    print(10 / 0)
except:
    print("Error occurred")
finally:
    print("Finally block executed")


#things to remember when in function prints something after returning it executes the final block for eg:


def try_function(n):
    a=10
    try:
        c=a/n
        print(c)
        return c
    except:
        print("Number cannot be zero" )
    finally:
        print("I am printed no matter what happened:")     


try_function(0)
