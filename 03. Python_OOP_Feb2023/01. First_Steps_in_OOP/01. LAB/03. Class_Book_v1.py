
class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages


# #####################################
# Test_Code_1:
book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)
# -------------------------------------
# My Book
# Me
# 200
# #####################################
