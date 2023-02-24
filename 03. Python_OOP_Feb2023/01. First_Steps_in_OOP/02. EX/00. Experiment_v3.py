
class Shop:
    def __init__(self, name, items):
        self.name = name
        self.items = items

    def get_items_count(self):
        items_count = len(self.items)
        return items_count


# ############################################################
# Test_Code_1:
shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
print(shop.get_items_count())
# -----------------------------------------------------------
# Output_1:
# 3
# ############################################################
