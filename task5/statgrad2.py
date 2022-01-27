for i in range(1000):
    if abs(sum(filter(lambda x: x % 2 == 0, map(int, str(i)))) - sum(map(int, str(i)[::-1]))) == 9:
        print(i)

