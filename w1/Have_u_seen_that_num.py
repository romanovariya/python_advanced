nums_line = input().split()
s = set()
for i in nums_line:
    if i in s:
        print('YES')
    else:
        print('NO')
    s.add(i)
