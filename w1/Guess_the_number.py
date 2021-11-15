n = int(input())
conceived_numbers = set(range(1, n + 1))
while True:
    input_line = input()
    if input_line == 'HELP':
        break
    input_line = {int(x) for x in input_line.split()}
    answer = str(input())
    if answer == 'YES':
        conceived_numbers.intersection_update(input_line)
    else:
        conceived_numbers.difference_update(input_line)
print(*sorted(conceived_numbers), sep=' ')
