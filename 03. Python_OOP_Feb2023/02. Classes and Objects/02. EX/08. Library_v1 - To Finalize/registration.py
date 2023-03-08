from project.user import User
from project.library import Library

from user import User
from library import Library

class Registration:
    def __init__(self):
        pass

    def add_user(self, user: User, library: Library):
        if user in library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        library.user_records.append(user)

    def remove_user(self, user: User, library: Library):
        