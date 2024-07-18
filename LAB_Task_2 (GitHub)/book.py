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
        
    def update(self, title=None, author=None, year=None, genre=None):
        if title:
            self.title = title
        if author:
            self.author = author
        if year:
            self.year = year
        if genre:
            self.genre = genre
    
book1 = book("Harry Potter","J.K. Rowling",1995,"Fantasy")
book2 = book("The Hobbit","	J. R. R. Tolkien",1937,"High fantasy, Children's fantasy")
book3 = book("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction")

booklist = [book1, book2, book3]

for i in booklist:
    i.display()
    
book1.update(year=1997)
print("Updated information of Book1")
book1.display()
