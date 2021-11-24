km = sorted(enumerate(map(int, input().split())), key=lambda x: x[1])
fares = sorted(enumerate(map(int, input().split())),
               key=lambda x: x[1], reverse=True)

values_tuple = sorted(zip(km, fares), key=lambda x: x[0][0])
res = map(lambda x: x[1][0], values_tuple)
print(*res, sep=' ')
