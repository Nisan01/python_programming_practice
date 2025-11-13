#here are different programs related to string like prefix check ,postfix check and soon

a="Nishan"
b="Nisha"

print(a[:len(a)])
print(a[:5])

c=""

for i in range(len(a)):
    if i<len(b) and  a[i]==b[i]:
        c=c+a[i] 
    else:    
     break    



print(c)



ar1=["flower","flow","fly"]

sample=ar1[0]

for x in ar1[1:]:
   
   while not x.startswith(sample):
      sample=sample[:-1]
   if sample =="":
      break    
   

print(sample)   

name = "nishan"
name2 = "roshan"

# Convert strings to sets of letters for printing common letters
common_letters = set(name) & set(name2)
print(common_letters)
print("Common letters:", "".join(common_letters))     


c=""

for chars in name:
   if chars in name2 and chars not in c:
      c+=chars
print(c)


#print if the middle characters 

name4="nisha"


c2=len(name4)

if c2 % 2 != 0:
   d=(c2-1)//2
   print(name4[d])
else:
   d=int(c2/2)
   print(name4[d-1]+name4[d])

#reverse of a string 

a12="NISHAN"
x=len(a12)
y=len(a12)-1

c=""

while(y>=0):
 c+=a12[y]
 y=y-1

print(c)

print(a12[::-1])

#using for loop 

d1=""
for x in range(len(a12)-1,-1,-1):
     d1+=a12[x]

print(d1)

aq=12345
c=str(aq)

print("last",''.join(reversed(c)))

#using next method
num=35648

rev=0
while(num>0):
   digit=num%10
   rev=rev*10+digit

   num//=10

print(rev)