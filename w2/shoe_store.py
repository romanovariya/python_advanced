foot_size = int(input())
sizes = sorted([int(x) for x in input().split()])

count = 0
previous_size = foot_size - 3

for i in sizes:
    if i >= previous_size + 3:
        previous_size = i
        count += 1
print(count)
