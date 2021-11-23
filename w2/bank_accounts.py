system_data = dict()
output = []

while True:
    input_line = input()
    if input_line == '':
        break
    input_line = input_line.split()
    command = input_line[0]
    if command == 'DEPOSIT':
        name = input_line[1]
        amount = input_line[2]
        if name not in system_data:
            system_data[name] = int(amount)
        else:
            system_data[name] += int(amount)
    elif command == 'WITHDRAW':
        name = input_line[1]
        amount = input_line[2]
        if name not in system_data:
            system_data[name] = -int(amount)
        else:
            system_data[name] -= int(amount)
    elif command == 'TRANSFER':
        name_1 = input_line[1]
        name_2 = input_line[2]
        amount = input_line[3]
        if name_1 not in system_data:
            system_data[name_1] = -int(amount)
        else:
            system_data[name_1] -= int(amount)
        if name_2 not in system_data:
            system_data[name_2] = int(amount)
        else:
            system_data[name_2] += int(amount)
    elif command == 'INCOME':
        interest = int(input_line[1])
        interest_rate = 1 + interest/100
        for key, value in system_data.items():
            if value >= 0:
                system_data[key] *= interest_rate
                system_data[key] = int(system_data[key])
    elif command == 'BALANCE':
        name = input_line[1]
        if name in system_data:
            output.append(system_data[name])
        else:
            output.append('ERROR')
print(*output, sep="\n")
