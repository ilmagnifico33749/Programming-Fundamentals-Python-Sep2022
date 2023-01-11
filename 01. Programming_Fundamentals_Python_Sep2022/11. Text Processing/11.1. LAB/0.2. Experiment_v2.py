x = 'apples'
y = 'lemons'
z = "In the basket are %s and %s" % (x, y)
print(z)
w = "In the basket are {} and {}".format(x, y)
print(w)

b = w[-6:]
print(b)

c = w[18:25]
print(c)
d = w[slice(18, 25, 1)]
print(d)