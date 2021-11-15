lang_list = set()

students_amount = int(input())

for i in range(1, students_amount + 1):
    lang_num = int(input())
    lang_input = set()
    for j in range(1, lang_num + 1):
        language = input()
        lang_input.add(language)
    lang_list.update(lang_input)
print(len(lang_list))
print(*sorted(lang_list), sep='\n')
