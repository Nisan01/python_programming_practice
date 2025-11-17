
#after completing the ,for loop the else block is executed

for i in range(5):
    print(i)
else:
    print("loop completed")

print("Out of the loop:")    



#Answer this 
 

for i in range(5):
    print(i)
    if i == 3:
        break
else:
    print("loop completed")

print("Out of the loop:")    
