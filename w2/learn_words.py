num = int(input())

word_list = [input() for _ in range(0, num)]

sorted_list = sorted(word_list,
                     key=lambda x: (len(x), x[::-1]))
print(*sorted_list, sep='\n')
