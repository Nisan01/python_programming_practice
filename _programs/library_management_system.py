

class Library:
    def __init__(self):
        self.booksList=[]
        self.booksNumber=0
        

    def addBooks(self,book):
        self.booksList.append(book)
        self.booksNumber+=1


    def viewBooks(self):

        for x in self.booksList:
            print(x) 

    def totalBooks(self):
        print(f"Total No. Of Books:{self.booksNumber}")


s1=Library()
s1.addBooks("Hum tere Bin")
s1.addBooks("jo tum mere ho")
s1.addBooks("Bagaicha")

print("----------List of Books :--------------")
s1.viewBooks()   
s1.totalBooks() 




