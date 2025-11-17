#factorial printing program
'''
a=int(input("Enter a number :"))

b=1

for x in range(a+1):
 
 b=b*x



print(b)

'''

#factorial using while loop
'''

a=int(input("Enter a number :"))
b=1
i=1

while(i<=a):

   b=b*i
   i=i+1

print(b)

'''

#for loop with dictionary

list={"name":"nishan","age":"10","address":"kathmandu"}

print(list["name"])
print(list["age"])

for key,value in list.items():
    print(key,":",value)


#while loop to take 4 inputs and display those inputs
'''
c=1
b=[]

while(c<=5):
 a=input("Enter your name")
 b.append(a)
 c=c+1

d=0

while(d<5):
   print(b[d]) 
   d=d+1

'''

#break and continue 

#break , break out from the loop and continue skips the iteration and continues the loop


for e in range(5):
   print("using break",e)
   if(e==4):
      break
   
for w in range(10):
  

        if(w==4):
             print("skip the iteration")  
             continue
        print(w)   
