n = int(input())
august_numbers = set(range(1, n + 1))
output = []
while True:
    input_line = input()
    if input_line == 'HELP':
        break
    input_line = {int(x) for x in input_line.split()}
    if len(input_line.intersection(august_numbers))\
            <= (len(august_numbers) / 2):
        august_numbers.difference_update(input_line)
        output.append('NO')
    else:
        august_numbers.intersection_update(input_line)
        output.append('YES')
print(*output, sep='\n')
print(*sorted(august_numbers), sep=' ')
