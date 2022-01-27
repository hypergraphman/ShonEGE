from itertools import product


alf = 'КЛРТ'
for i, word in enumerate(product(alf, repeat=4), start=1):
    word = ''.join(word)
    if word == 'ШКОЛА':
        print(i)
    if i == 67:
        print(word)