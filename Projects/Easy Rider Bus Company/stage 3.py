import json
data = json.loads(input())
line_stops = []
for i in data:
    for key, value in i.items():
            if key == "bus_id" and i["stop_type"] in ["S", "O", "F", ""]:
                line_stops.append(value)

res = {}
for j in line_stops :
    res[j] = line_stops.count(j)

print("Line names and number of stops:")
for m, l in res.items():
    print(f"bus_id: {m}, stops: {l}")
