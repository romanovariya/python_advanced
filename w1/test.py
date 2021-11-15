counts = {'USA': 2, 'France': 2, 'Germany': 1}
countries = {value: key for key, value in counts.items()}
print(len(countries), countries)