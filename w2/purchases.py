customers_list = {}

while True:
    line = input()
    if line == '':
        break
    line = line.split()
    name = line[0]
    item = line[1]
    quantity = int(line[2])
    if name not in customers_list:
        customers_list[name] = {}
        customers_list[name][item] = quantity
    else:
        if item in customers_list[name]:
            customers_list[name][item] += quantity
        else:
            customers_list[name][item] = quantity
sorted_customers = sorted(customers_list)
for customer in sorted_customers:
    sorted_items = sorted(customers_list[customer])
    print(f'{customer}:')
    for i in sorted_items:
        print(f'{i} {customers_list[customer][i]}')
