'''
Definition and Usage
The seek() method sets the current file position in a file stream.

The seek() method also returns the new postion.

'''

'''
Definition and Usage
The tell() method returns the current file position in a file stream.

Tip: You can change the current file position with the seek() method.

'''


file=open("hello.txt",'r')
cont=file.read()

if cont:
 print(cont,end='')

print("\nPointer after first read:", file.tell())
if cont:
 print(cont,end='')

print("\nPointer after 2nd read:", file.tell())


 





