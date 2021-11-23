distances = sorted([int(x) for x in input().split()])
prices = sorted([int(x) for x in input().split()], reverse=True)

res = 0
for i in range(0, len(prices)):
    amount = distances[i] * prices[i]
    res += amount

print(res)
