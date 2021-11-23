text = []
while True:
    input_line = input()
    if input_line == '':
        break

    input_line = input_line.split()
    for word in input_line:
        text.append(word)

dictionary = {}
output = []
for i in range(0, len(text)):
    key = dictionary.get(text[i])
    if key is None:
        output.append('-1')
        dictionary[text[i]] = text.index(text[i])
        text[i] = 0
    else:
        output.append(dictionary[text[i]])
        dictionary[text[i]] = str(i)
print(*output)
