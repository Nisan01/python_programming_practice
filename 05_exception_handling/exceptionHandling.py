

'''
Exception handling is the process of responding to unwanted or unexpected events when a 
computer program runs. Exception handling deals with these events to avoid the program or system crashing, 
and without this process, exceptions would disrupt the normal operation of a program.


try:
     #statements which could generate 
     #exception
except:
     #Soloution of generated exception

'''






try:
    a=int(input("Enter the multiplication of num : "))

    for i in range(10):
        print(f"{a} * {i+1} = {(a*(i+1))}")
except Exception:
    print("Please,enter only the number")
   


print("I want to print this anyhow")

#we can use multiple errors handling using multiple  except blocks

try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")