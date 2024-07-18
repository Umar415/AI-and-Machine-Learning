class book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        
    def display(self):
        print("Book Title: ", self.title)
        print("Book Author: ", self.author)
        print("Year of publish: ", self.year)
        print("Book genre: ", self.genre)
        print()

class library:
    def __init__(self):
        self.books = {}
    
    def add_book(self, books):
        self.books[books.title] = books
    
    def remove_book(self, title):
        if title in self.books:
            del self.books[title]
        else:
            print("Book not found")
    
    def find_book(self, title):
        if title in self.books:
            print("Book Found")
            self.books[title].display()
        else:
            print("Book not found")
    
    def listing(self):
        print("List of all books in Library")
        for i in self.books:
            self.books[i].display()
      
       
       
mylib = library()
     
book1 = book("Harry Potter","J.K. Rowling",1995,"Fantasy")
book2 = book("The Hobbit","	J. R. R. Tolkien",1937,"High fantasy, Children's fantasy")
book3 = book("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction")

mylib.add_book(book1)
mylib.add_book(book2)
mylib.add_book(book3)

mylib.find_book("The Hobbit")
mylib.listing()

mylib.remove_book("To Kill a Mockingbird")
mylib.listing()