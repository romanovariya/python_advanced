lines = int(input())
dictionary = dict()
errors = 0

for i in range(1, lines + 1):
    stress_word = input()
    if stress_word.lower() in dictionary:
        dictionary[stress_word.lower()].append(stress_word)
    else:
        dictionary[stress_word.lower()] = [stress_word]

input_line = input().split()

for word in input_line:
    if word.lower() in dictionary:
        if word in dictionary[word.lower()]:
            pass
        else:
            errors += 1
    else:
        upper_case = 0
        for i in word:
            if i == i.upper():
                upper_case += 1
        if upper_case != 1:
            errors += 1
print(errors)
