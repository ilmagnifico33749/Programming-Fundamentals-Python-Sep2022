def grocery_store(**kwargs):

    kwargs = (sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
    return '\n'.join([f"{name}: {quantity}" for name, quantity in kwargs])


# #####################
# Test_Code_1:
print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
# ---------------------
# Output_1:
# pasta: 12
# eggs: 12
# bread: 5
# #####################
# Test_Code_2:
print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
# ---------------------
# eggs: 20
# bread: 2
# pasta: 2
# carrot: 1
# #####################
