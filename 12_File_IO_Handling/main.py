

'''

        Modes in file
        There are various modes in which we can open files.

        read (r): This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter.

        write (w): This mode opens the file for writing only and creates a new file if the file does not exist.

        append (a): This mode opens the file for appending only and creates a new file if the file does not exist.

        create (x): This mode creates a file and gives an error if the file already exists.

        text (t): Apart from these modes we also need to specify how the file must be handled. t mode is used to handle text files. t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the default. The default mode is 'r' (open for reading text, synonym of 'rt' ).

        binary (b): used to handle binary files (images, pdfs, etc).

'''

write=open("nisan.txt","w")
write.write("Hello Nishan")
write.close()

readFile=open("nisan.txt",'r')

print(readFile.read())


#Keep in mind that writing to a file will overwrite its contents.
#  If you want to append to a file instead of overwriting it, you can open it in append mode.

#Alternatively, you can use the with statement to automatically close the file after you are done with it.

'''

with open('myfile.txt', 'r') as f:
    # ... do something with the file

'''



f=open("marks.txt",'r')


for i in range(3):
 line=f.readline()
 m1=line.split(",")[0]
 m2=line.split(",")[1]
 m3=line.split(",")[2]
 


 std="Nishan" if i==0 else "Roshan" if i==1 else "Rajat"  

 print(f"Student {std} subject in Maths is :{m1}")
 print(f"Student {std} subject in Science is :{m2}")
 print(f"Student {std} subject in GK is :{m3}")

 


#out of for loop
print("Out of the loop")

f.seek(0)

read=f.readline()


print(repr(read))
print(read)
print(read)
