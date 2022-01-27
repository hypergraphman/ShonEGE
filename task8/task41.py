from itertools import product

alf = 'kran'
c = 0
for word in product(alf, repeat=3):
    word = ''.join(word)
    if 'a' in word:
        c += 1
print(c)
