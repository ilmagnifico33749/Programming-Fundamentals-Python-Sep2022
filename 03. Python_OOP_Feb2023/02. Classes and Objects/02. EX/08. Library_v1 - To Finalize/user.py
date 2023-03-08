class User:
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books = list()

    def info(self):
        return ', '.join(sorted(self.books, key=lambda x: x[0], reverse=False))

    def __str__(self):
        # override the method to get a string in the following format:
        # "{user_id}, {username}, {list of rented books}"


