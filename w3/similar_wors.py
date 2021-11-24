words = input().split()
scores = input().split()

table = list(zip(words, scores))
filtered_table = list(filter(lambda x: float(x[1]) > 0.5, table))
output = sorted(filtered_table, key=lambda x: x[1], reverse=True)
words_list = map(lambda x: x[0], output)
print(*words_list, sep='\n')
