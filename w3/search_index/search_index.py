import json

words_num = int(input())
words_arr = [input() for _ in range(words_num)]
output_file = input()

result = dict()
first_set = []
second_set = []
for elem in words_arr:
    first_set.append(elem[0])
first_set = list(dict.fromkeys(first_set))
for elem in first_set:
    result[elem] = {}
    for word in words_arr:
        if elem == word[0]:
            second_set.append(elem + word[1])
second_set = list(dict.fromkeys(second_set))

sorted_words = sorted(words_arr)
for obj, value in result.items():
    for i in second_set:
        if obj == i[0]:
            arr = []
            for word in sorted_words:
                if word[0:2] == i:
                    arr.append(word)
            result[obj][i] = sorted(arr)

with open(output_file, 'w') as file:
    json.dump(result, file)
