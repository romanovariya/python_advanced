word_count_dict = dict()
answers = []

while True:
    input_line = input()
    if input_line == '':
        break

    for word in input_line.split():
        if word not in word_count_dict:
            word_count_dict[word] = 0

        answers.append(word_count_dict[word])
        word_count_dict[word] += 1

print(*answers, sep=' ')
