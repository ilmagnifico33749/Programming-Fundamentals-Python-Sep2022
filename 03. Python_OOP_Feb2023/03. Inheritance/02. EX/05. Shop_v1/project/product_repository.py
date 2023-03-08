from project.product import Product
# from product import Product

class ProductRepository:
    def __init__(self):
        self.products = list()

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name):
        searched_product = self.find(product_name)

        if searched_product:
            self.products.remove(searched_product)

    def __repr__(self):
        return '\n'.join([f"{product.name}: {product.quantity}" for product in self.products])
