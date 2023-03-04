class Glass:
    capacity = 250
    def __init__(self):
        self.content = 0

    def fill(self, ml):
        if self.content + ml < self.capacity:
            self.content = ml
            return f"Glass filled with {ml} ml"
        else:
            return f"Cannot add {ml} ml"

    def empty(self):
        self.content = 0
        return f"Glass is now empty"

    def info(self):
        return f"{self.capacity - self.content} ml left"


# #########################
# Test_Code:
glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
# ------------------------
# Output_1:
# Glass filled with 100 ml
# Cannot add 200 ml
# Glass is now empty
# Glass filled with 200 ml
# 50 ml left
# #########################
