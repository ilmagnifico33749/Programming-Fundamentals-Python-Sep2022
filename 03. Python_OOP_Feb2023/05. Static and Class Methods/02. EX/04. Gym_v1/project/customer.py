class Customer:
    customer_id = 1
    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email

    @staticmethod
    def get_next_id():
        next_customer_id = Customer.customer_id + 1
        return next_customer_id

    def __repr__(self):
        return f"Customer <{self.customer_id}> {self.name}; Address: {self.address}; Email: {self.email}"

