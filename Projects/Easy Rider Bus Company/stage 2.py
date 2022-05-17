import json
import re
data = json.loads(input())
mistakes = {"stop_name": 0, "stop_type": 0, "a_time": 0}
pattern_time = re.compile(r"^([01][0-9]|2[0-3]):([0-5][0-9])$")
pattern_name = re.compile(r"((^[A-Z][a-z]+)|(^[A-Z][a-z]+) (\w+)) (Road|Avenue|Boulevard|Street)$")

for i in data:
    if (not isinstance(i["stop_name"], str)) or re.match(pattern_name, i["stop_name"]) is None:
        mistakes["stop_name"] += 1
    if (not isinstance(i["a_time"], str)) or re.match(pattern_time, i["a_time"]) is None:
        mistakes["a_time"] += 1
    if (not isinstance(i["stop_type"], str)) or i["stop_type"] not in ["S", "O", "F"]:
        if i["stop_type"] != "":
            mistakes["stop_type"] += 1


print(f"Format validation: {sum(mistakes.values())} errors")
for key, values in mistakes.items():
    print(key + ":", values)
