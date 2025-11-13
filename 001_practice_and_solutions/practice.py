

A="NISAHAN"


c=2
print(A)
print(c)
print(type(A))
print(type(c))

def add(a,b):
    return a+b

print(add(4,5))


b=45

print(type(b))

c=str(b)
print(type(c))

a=45

print(a>b)
print(a<=b)
#a<b

"""

a==b
this is a multi line comment .so we can write anything here no problem guuys hey how are you all doing

"""


text="123"

if text.isdigit():

    c=int(text)
    print (c)
    print(type(c))

else:
        print("not a number")
    




'''


name=input("Enter your name :")

print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())
print(name.strip())
print(name.replace("a","@"))
print(name.find("a"))

print(name[::-1])

'''

phoneNumber=98154

print(type(phoneNumber))


f=str(phoneNumber)[::-1]
print(f)
print(type(f))

print(type(phoneNumber))


def reverse(num):
     return str(num)[::-1]


print(reverse(12345))
print(reverse(9876543210))
print(reverse(4567891230))


def reversed(reverseLine):
     
     if type(reverseLine) == int:
          return str(reverseLine)[::-1]
     else:
          return reverseLine[::-1]
     
print(reversed(12345))
print(reversed("Nisahan"))
print(reversed("Hello World"))


name1="Nisahan"
print(name1[0])
print(name1[-1])
print(name1[0:4])

print(name1[0:-1])

print(name1[0:7:2])


coll={"name":"Nishan", "age":20, "address":"Kathmandu"}
print(coll["name"])
print(coll["age"])
print(coll["address"])



for key in coll:
    print(key, ":", coll[key])


list1=[1,2,3,4,5,6,7,8,9]
print(list1[0])
print(list1[-1])
print(list1[0:5])
print(list1[::-1])

cef=list1.reverse()
print(type(cef))
print(list1)