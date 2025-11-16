#function to print name 

def print_name(name):
    print(f"Hello {name}")


print_name("nishan")

#the default parameter value should always come after non default arguments
def print_name2(fname,lastname,midName="Kiran"):
    print(f"This is {fname} {midName} {lastname}")


print_name2("Nishan","Chauhan")
print_name2("Nishan","Chauhan","prasad")



#variable length arguments 

def average_numbers(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    
    print("Average",sum/len(numbers))


average_numbers(4,5,7,8,9)
average_numbers(2,3)

#time for dictionery in arguments

def dictionery_arguments(**person):
    print(f"This is\n{person['fname']} {person['age']} {person['address']}")


dictionery_arguments(fname="Nishan",age="22",address="Chabahil")
