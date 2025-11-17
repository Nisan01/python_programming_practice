
#Recursion is a functions that calls function within the function 


def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    

print(factorial(5))


#fibonacci series

def fibonacci_series(num):
    a,b=0,1
    for i in range(num):
        print(f"{a}",end=" ")
        a,b=b,a+b
        
        
        


fibonacci_series(10)



#reverse of a string using recursion

def reverse_string(name):
    if len(name)==0:
        return""
    else:
        return reverse_string(name[1:]) + name[0]



print(reverse_string("nishan"))

name2="Rajesh"
print(name2[1:])


def fibonacci_series_recursion(number):
    if number <= 1:
        return number
    else:
        return fibonacci_series_recursion(number-1)+fibonacci_series_recursion(number-2)


x=fibonacci_series_recursion(3)
print(x)