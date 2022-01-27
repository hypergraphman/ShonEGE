from itertools import product

alf = 'ABCD'
for word in product(alf, repeat=3):
    word = ''.join(word)

