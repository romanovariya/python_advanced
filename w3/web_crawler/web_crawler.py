import json

filename = input()
res = []
with open(filename) as file:
    data = json.loads(file.readline())


def iterate(item, url=''):
    if item == dict():
        res.append(url[1:])
    else:
        for k in item:
            iterate(item[k], f'{url}/{k}')


iterate(data)

print(*sorted(res), sep='\n')
