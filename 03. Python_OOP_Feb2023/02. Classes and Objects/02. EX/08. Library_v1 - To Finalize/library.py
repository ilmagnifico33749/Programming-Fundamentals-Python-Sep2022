# from project.user import User
from user import User

class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        # ^ {"authors"(key: str): books(list: str)}
        self.rented_books = {}
        # ^ {"username": {"book_name"(key:str): days_to_return(int)}}

        def get_book(author: str, book_name: str, days_to_return: int, user: User):
            if book_name in self.rented_books[author].values():
                return f"The book {book_name} is already rented and will be available in " \
                       f"{self.rented_books[author]['days_to_return']} days!"
            user.books.append(book_name)
            self.books_available[author].remove(book_name)
            self.rented_books[user.username] = {book_name: days_to_return}

        def return_book(author: str, book_name: str, user: User):
            if book_name in user.books:
                self.rented_books[user.username].remove(book_name)
                self.books_available[author].append(book_name)
            else:
                return f"{user.username} doesn't have this book in his/her records!"


