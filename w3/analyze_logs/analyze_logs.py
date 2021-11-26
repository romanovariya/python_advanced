import json

errors = 0
msg_correct_200 = 0
msg_correct = 0
msg_status_not_int = 0
msg_no_status = 0

filename = input()

with open(filename) as file:
    for line in file:
        try:
            logs = json.loads(line)
        except json.decoder.JSONDecodeError:
            errors += 1
        else:
            status = logs.get('status')
            try:
                status = int(status)
            except ValueError:
                if status == '':
                    msg_no_status += 1
                else:
                    msg_status_not_int += 1
            except TypeError:
                msg_no_status += 1
            else:
                if status == 200:
                    msg_correct_200 += 1
                else:
                    msg_correct += 1
print(msg_correct_200, msg_correct, msg_status_not_int,
      msg_no_status, errors, sep='\n')
