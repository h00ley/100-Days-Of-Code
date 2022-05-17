import json
data = json.loads(input())

stops = {"S" : set(), "F" : set(), "T" : set()}
bus_stops = {}
buses = {}
stop_times = {}

for i in data:
    if i["stop_type"] == "S" or i["stop_type"] == "F" :
        stops[i["stop_type"]].add(i["stop_name"])
        buses.setdefault(i["bus_id"], {"S" : [], "F" : []})
        buses[i["bus_id"]][i["stop_type"]].append(i["stop_name"])

    bus_stops.setdefault(i["bus_id"], set())
    bus_stops[i["bus_id"]].add(i["stop_name"])
for value in bus_stops.values() :
    for stop in value :
        stop_times.setdefault(stop, 0)
        stop_times[stop] += 1
for stop in stop_times :
    if stop_times[stop] > 1 :
        stops["T"].add(stop)


def count_stops() :
    for bus_id in bus_stops :
        print(f'bus_id: {bus_id}, stops: {len(bus_stops[bus_id])}')


def start_trans_final() :
    for line in buses :
        if len(buses[line]["S"]) != 1 or len(buses[line]["F"]) != 1 :
            print(f"There is no start or end stop for the line: {line}.")
            return

    print(f'''Start stops: {len(stops["S"])} {sorted(list(stops["S"]))}
Transfer stops: {len(stops["T"])} {sorted(list(stops["T"]))}
Finish stops: {len(stops["F"])} {sorted(list(stops["F"]))}''')

start_trans_final()