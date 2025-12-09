
'''
The filter() function returns an iterator where the items are filtered through a 
function to test if the item is accepted or not.

'''


# Filter the array, and return a new array with only the values equal to or above 18:
ages = [5, 12, 17, 18, 24, 32]

newarray=[]

for item in ages:
    if(item>=18):
        newarray.append(item)


print(newarray)



ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)

for x in adults:
  print(x)



dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

a=[]

for x in dromes:
   if(x==x[::-1]):
      a.append(x)
print(a)  


palindrome=list(filter(lambda item:item==item[::-1],dromes))
print(palindrome)



   
checkPalin=lambda item:item if item==item[::-1] else None

for y in dromes:
   z=checkPalin(y)
   if z:
    print(z)

      