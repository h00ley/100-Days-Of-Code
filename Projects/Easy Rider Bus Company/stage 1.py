import json
from collections import Counter
json_to_py = json.loads(input())
mistakes = []
for i in json_to_py:
    for field in i:
        if field in ["bus_id", "stop_id", "next_stop"] and type(i[field]) != type(int()):
            if bool(i[field]) is False and not field:
                print(field, type(i[field]), bool(i[field]))
                mistakes.append(field)
            mistakes.append(field)
        if field in ["stop_name", "a_time"]:
            if bool(i[field]) is False or type(i[field]) != type(str()):
                mistakes.append(field)
        if field in ["stop_type"]:
            if type(i[field]) != type(str()) or len(i[field]) > 1:
                mistakes.append(field)

count = Counter(mistakes)
k = {}
for key, value in count.items():
    k[key] = value

print(f'Type and required field validation: {len(mistakes)} errors')
if len(mistakes) > 0:
    print([key for key in k.keys()][3] + ':', [value for value in k.values()][3])
    print([key for key in k.keys()][2] + ':', [value for value in k.values()][2])
    print([key for key in k.keys()][1] + ':', [value for value in k.values()][1])
    print([key for key in k.keys()][4] + ':', [value for value in k.values()][4])
    print([key for key in k.keys()][5] + ':', [value for value in k.values()][5])
    print([key for key in k.keys()][0] + ':', [value for value in k.values()][0])
else:
    print('bus_id' + ':', 0)
    print('stop_id' + ':', 0)
    print('stop_name' + ':', 0)
    print('next_stop' + ':', 0)
    print('next_stop' + ':', 0)
    print('a_time' + ':', 0)