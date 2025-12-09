

w=open("writeline.txt",'w')

lines=['Nisan is a boy\n','Nisan is not a gay\n','Nishan likes playing']

w.writelines(lines)
w.close()

print("Added lines successfully")


r=open("writeline.txt",'r')




# read=r.readlines()
# print(read)

# for it in read:
#     print(it)

for i in range(3):
    read=r.readline()
    print(read)

