import json
file_names = input().split()
output_file = input()

logs = list()

for file in file_names:
    with open(file) as f:
        logs += list(map(lambda x: json.loads(x.rstrip()), f.readlines()))

logs.sort(key=lambda line: (line['date'], line['consumer_id']))
with open(output_file, 'w') as output:
    for row in logs:
        output.write(row["date"])
        output.write("\t")
        output.write(row["message"])
        output.write("\n")
