countries_amount = int(input())
countries = dict()
for i in range(1, countries_amount + 1):
    country_line = input().split()
    country_name = country_line[0]
    cities = country_line[1:]
    for j in range(0, len(cities)):
        countries[cities[j]] = country_name
questions = int(input())
to_print = []
for i in range(1, questions + 1):
    capital = input()
    to_print.append(countries[capital])


print(*to_print, sep='\n')
