class Shop:
    def __init__(self, name: str, shop_type: str, capacity: int):
        self.name = name
        self.shop_type = shop_type
        self.capacity = capacity
        self.items = dict()

    @classmethod
    def small_shop(cls, name: str, shop_type: str):
        return cls(name, shop_type, 10)

    def add_item(self, item_name: str):
        if len(self.items) + 1 > self.capacity:
            return f"Not enough capacity in the shop"

        else:
            if item_name not in self.items.values():
                self.items[item_name] = 0
                return f"{item_name} added to the shop"
            self.items[item_name] += 1

    def remove_item(self, item_name: str, amount: int):
        if item_name not in self.items:
            return f"Cannot remove {amount} {item_name}"
        else:
            amount_to_be_removed = 0
            if (self.items[item_name] - amount) <= 0:
                self.items.pop(item_name)
            else:
                self.items[item_name] -= amount
            return f"{amount} {item_name} removed from the shop"

        def __repr__(self):
            return f"{self.name} of type {self.shop_type} with capacity {self.capacity}"

# ############################################################
# Test_Code_1:
fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
print(fresh_shop)
print(small_shop)
print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Tomatoes", 2))
print(small_shop.add_item("Jeans"))
print(small_shop.add_item("Jeans"))
print(small_shop.remove_item("Jeans", 2))
print(small_shop.items)
# -------------------------------------------------------------
# Output_1:
# Fresh Shop of type Fruit and Veg with capacity 50
# Fashion Boutique of type Clothes with capacity 10
# Bananas added to the shop
# Cannot remove 2 Tomatoes
# Jeans added to the shop
# Jeans added to the shop
# 2 Jeans removed from the shop
# {}
# ############################################################
