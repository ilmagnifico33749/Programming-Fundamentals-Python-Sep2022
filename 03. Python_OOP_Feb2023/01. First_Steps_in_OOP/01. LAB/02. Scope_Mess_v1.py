# ###########
# #Original Code to be corrected:
x = "global"

def outer():
    x = "local"

    def inner():
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()

print(x)
outer()
print(x)
# ----------------------------------
# Original Output:
# global
# outer: local
# inner: nonlocal
# outer: local
# global
# ---------------------------------
# ##################################
# #Required Output:
# global
# outer: local
# inner: nonlocal
# outer: nonlocal
# global: changed!
# ----------------------------------------
# #Corrected Code
x = "global"

def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        global x
        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()

print(x)
outer()
print(x)
######
