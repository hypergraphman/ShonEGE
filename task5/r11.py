def avt(n):
    d1 = bin(n)[2:]
    d2 = int(d1[1:], 2)
    return n - d2


res = set()
for i in range(500, 5000 + 1):
    res.add(avt(i))
print(len(res))