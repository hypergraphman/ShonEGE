from itertools import product


alf = 'ЕГЭ'
count = 0
for word in product(alf, repeat=5):
    word = ''.join(word)
    if word[0] in 'ЕЭ':
        count += 1
print(count)