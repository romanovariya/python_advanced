unique_words = {}

while True:
    input_line = input()
    if input_line == '':
        break
    input_line = input_line.split()
    for i in input_line:
        if i in unique_words:
            unique_words[i] += 1
        else:
            unique_words[i] = 1

new_sort = sorted(unique_words, key=lambda x: (-unique_words.get(x), x))
print(*new_sort, sep='\n')
