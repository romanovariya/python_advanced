days_data = input().split()

year = int(days_data[0])
parties = int(days_data[1])
saturdays = {n for n in range(6, year+1, 7) if n <= year}
sundays = {n for n in range(7, year+1, 7) if n <= year}
weekends = saturdays.union(sundays)
strike_days = set()
for party in range(1, parties + 1):
    party_data = input().split()
    party_start = int(party_data[0])
    party_int = int(party_data[1])
    party_strikes = set()
    i = party_start
    while i <= year:
        party_strikes.add(i)
        i += party_int
    strike_days.update(party_strikes)
strike_days.difference_update(weekends)
print(len(strike_days))
