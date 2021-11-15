lines = int(input())
dictionary = dict()
for i in range(1, lines + 1):
    pair = input().split()
    dictionary[pair[0]] = pair[1]
    dictionary[pair[1]] = pair[0]
synonym = input()
print(dictionary[synonym])
