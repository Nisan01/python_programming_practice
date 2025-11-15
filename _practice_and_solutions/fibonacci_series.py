# Fibonacci using for loop
a = 0
b = 1
n = 10

print("Using for-loop:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

# Reset values
a = 0
b = 1
n = 10

print("\nUsing while-loop:")
while n > 0:
    print(a, end=" ")
    a, b = b, a + b
    n -= 1

#using function 

print("\nfibonacci series using function")

def fibonacci_series(f):
    a=0
    b=1
    result=[]
    for i in range(f):
        print(a,end=" ")
        result.append(a)
        a,b=b,a+b

    return result    
        

series=fibonacci_series(12)

print(f"\n{series}")