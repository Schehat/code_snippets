a, b = (1, 2)
print(a, b)

a, _ = (1, 2)
print(a)

a, b, *c = (1, 2, 3, 4, 5, 6)
print(a, b, c)

a, b, *_ = (1, 2, 3, 4, 5, 6)
print(a, b)
