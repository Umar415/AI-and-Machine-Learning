dic_book = {
    1 : {"Title" : "Harry Potter","Author" :"J.K. Rowling", "Year":1995, "Genre" : "Fantasy"},
    2 : {"Title": "To Kill a Mockingbird", "Author": "Harper Lee", "Year": 1960, "Genre": "Southern Gothic"},
    3 : {"Title": "The Catcher in the Rye", "Author": "J.D. Salinger", "Year": 1951, "Genre": "Coming-of-age fiction"},
    4 : {"Title": "Pride and Prejudice", "Author": "Jane Austen", "Year": 1813, "Genre": "Romance novel"},
    5 : {"Title": "The Great Gatsby", "Author": "F. Scott Fitzgerald", "Year": 1925, "Genre": "Tragedy, Modernist novel"}
}

def addbook(title, author, year, genre):
    dic_book[len(dic_book)+1] = {"Title" : title, "Author" : author, "Year" : year, "Genre" : genre}


def rembook(bookid):
    if bookid in dic_book:
        del dic_book[bookid]
            
def updatebook(bookid, title=None, author=None, year=None, genre=None):
    if bookid in dic_book:
        if title:
            dic_book[bookid]["Title"] = title
        if author:
            dic_book[bookid]["Author"] = author
        if year:
            dic_book[bookid]["Year"] = year
        if genre:
            dic_book[bookid]["Genre"] = genre
    
    
addbook("python", "umar", 2012, "study")

rembook(3)

updatebook(1, year=1997)

for key, i in dic_book.items():
    print("Book ID: ",key)
    print("Book Title: ",i["Title"])
    print("Book Author: ",i["Author"])
    print("Publish Year: ",i["Year"])
    print("Book Genre: ",i["Genre"])
    print()