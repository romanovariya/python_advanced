iterable_1 = input().split()
iterable_2 = input().split()

main_tuple = zip(iterable_1, iterable_2)
xor = {('0', '0'): '0', ('0', '1'): '1', ('1', '0'): '1', ('1', '1'): '0'}
output = list(map(lambda x: xor[x], list(main_tuple)))
print(*output, sep=" ")
