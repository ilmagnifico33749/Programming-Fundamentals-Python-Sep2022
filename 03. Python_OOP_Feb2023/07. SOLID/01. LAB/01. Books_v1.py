# ####################################################
# # Code_To_Correct_1:
# class Book:
#     def __init__(self, title, author, location):
#         self.title = title
#         self.author = author
#         self.location = location
#         self.page = 0
#
#     def turn_page(self, page):
#         self.page = page
# ####################################################
# Corrected_Code_1:
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __repr__(self):
        return f"Book: \n - Title: {self.title}\n - Author: {self.author}"


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = list()

    def add_book(self, book: Book):
        if book in self.books:
            return f"The book is already in {self.name}\n"
        self.books.append(book)
        return f"New book has been added to {self.name}!\n{str(book)}\n"

    def find_book_title(self, title):
        for book in self.books:
            if book.title == title:
                return f"Found the book!\n{book}"
####################################################
# Test_1:
library = Library("Home Library")
book_1 = Book("The Craft", "John Dickie")
book_2 = Book("The Lost Symbol", "Dan Brown")
book_3 = Book("Harry Potter: Legacy", "J.K.Rowling")
print(library.add_book(book_1))
print(library.add_book(book_2))
print(library.add_book(book_3))
print(library.add_book(book_3))
print(library.find_book_title("The Craft"))
####################################################
