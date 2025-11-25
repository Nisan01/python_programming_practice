#previously we used to do this

a=[20,30,45,565,90,67]


for item in range(len(a)):
    print(item)

    if(item==3):
        print("This is third index :")



print("")

index=0

for data in a:
    print(data)
    if(index==3):
        print("this is the third index")
        break
    index+=1


for indexData,marks in enumerate(a,start=1):
    print(f"{indexData} {marks}")    

