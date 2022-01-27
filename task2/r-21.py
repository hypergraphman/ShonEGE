from itertools import product

for x, y, z, w in product((0, 1), repeat=4):
    if (((x and (not y)) or (w <= z)) == (z == x)) == 1:
        print(z, y, w, x)