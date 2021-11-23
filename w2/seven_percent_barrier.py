order = []
votes_counter = {}
current = ''

while True:
    vote = input()
    if vote == '':
        break
    if vote == 'PARTIES:':
        current = 'parties'
    elif vote == 'VOTES:':
        current = 'votes'
    if current == 'parties':
        if vote != 'PARTIES:' and vote != 'VOTES:':
            order.append(vote)
            votes_counter[vote] = 0
    if current == 'votes':
        if vote != 'PARTIES:' and vote != 'VOTES:':
            votes_counter[vote] += 1

amount = 0
for values in votes_counter.values():
    amount += values
percentage = amount * 7 / 100
for item in order:
    if votes_counter[item] >= percentage:
        print(item)
