#reversing a string in python !!!

a="nishan"
d="chauhan"

e=a[0:3]+d[4:7]
print(e)

e=a+d
print(e)

b=589548
print(a[-1])

c=str(b)

rev="".join(reversed(c))

print(int(rev))

for i in range(1,7):
    print(f"{a[-i]}",end="")


print("")

i=len(a)-1
while(i>=0):
    print(a[i],end="")
    i-=1

