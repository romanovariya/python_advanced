text = []

while True:
    input_line = input()
    if input_line == '':
        break
    input_line = input_line.split()
    for i in range(0, len(input_line)):
        text.append(input_line[i])

counter = dict()

for i in range(0, len(text)):
    if text[i] in counter:
        counter[text[i]] += 1
    else:
        counter[text[i]] = 1
all_nums = []
for num in counter.values():
    all_nums.append(num)
max_val = max(all_nums)

output = []
for key, value in counter.items():
    if value == max_val:
        output.append(key)
output = sorted(output)
print(output[0])
