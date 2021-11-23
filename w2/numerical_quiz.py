num_amount = int(input())

num_list = [input() for _ in range(num_amount)]
num_dict = {}

for num in num_list:
    if len(num) % 2 == 0:
        iterations = int(len(num) / 2)
    else:
        iterations = int((len(num) - 1) / 2)
    start = 0
    end = len(num) - 1
    num_sum = 0
    for i in range(iterations):
        num_sum += int(num[start]) - int(num[end])
        start += 1
        end -= 1
    num_dict[num] = num_sum

sorted_list = sorted(num_dict, key=lambda x: (num_dict.get(x), int(x)))
print(*sorted_list, sep='\n')
