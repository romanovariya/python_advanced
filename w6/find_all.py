import re
res = list()

while True:
    line = input()
    if line == '':
        break
    search = re.findall(r'<i>(.*?)</i>', line)
    if search:
        res += search


print(*res, sep='\n')
