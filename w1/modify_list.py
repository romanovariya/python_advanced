def modify_list(a):
    a[:] = [int(x / 2) for x in a if x % 2 == 0]
