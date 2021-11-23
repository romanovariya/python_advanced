space, users_num = [int(x) for x in input().split()]
users_data = sorted([int(input()) for _ in range(users_num)])

used_space = 0
count = 0
for i in users_data:
    if used_space + i <= space:
        count += 1
        used_space += i

print(count)
