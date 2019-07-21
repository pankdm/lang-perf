import numpy as np
import matplotlib.pyplot as plt

from collections import defaultdict
import json

class MapInfo:
    def __init__(self):
        self.nodes = 0
        self.edges = 0


data = defaultdict(dict)
maps = {}
map_infos = {}

f = open('results.txt', 'r')
total = 0
for line in f.xreadlines():
    j = json.loads(line)

    # skip tiny maps
    if j["edges"] < 100:
        continue

    # skip duplicate
    if j["map"] == "vancouver.txt":
        continue

    total += 1
    data[j["name"]][j["map"]] = float(j["time"])
    maps[j["map"]] = j["edges"]

    map_info = MapInfo()
    map_info.nodes = j["nodes"]
    map_info.edges = j["edges"]
    map_infos[j["map"]] = map_info

maps_list = sorted(maps.keys(), key=lambda x: maps[x])
# print (maps_list)


def get_values_list(values, maps_list, baseline):
    result = []
    for m in maps_list:
        result.append(values[m] / baseline[m])
    return result


def print_maps():
    counter = 0
    # header = ", ".join(sorted(data.keys()))
    # print (header)

    for m in maps_list:
        print("{}: {} v={} e={}".format(
            counter, m, map_infos[m].nodes, map_infos[m].edges))
        counter += 1
print_maps()

def print_csv():
    tags = sorted(data.keys())
    print ("")
    print ("map, vertices, edges, {}".format(", ".join(tags)))
    for m in maps_list:
        baseline = data["cpp"][m]
        values = [data[tag][m] for tag in tags]
        values_print = ", ".join(map(lambda x : ("%.2f" % x), values))
        print("{}, {}, {}, {}".format(
            m, map_infos[m].nodes, map_infos[m].edges, values_print))

print_csv()

x = range(len(maps_list))

fig, ax = plt.subplots()

palette = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'skyblue', 'burlywood']
num = 0
for tag in data.keys():
    y = get_values_list(data[tag], maps_list, data["cpp"])
    c = palette[num]

    LOG_SCALE = False
    if LOG_SCALE:
        ax.semilogy(x, y, marker='o', color=c, label=tag)
    else:
        plt.plot(x, y, marker='o', color=c, label=tag)

    num += 1
ax.grid()
plt.legend(loc=1, ncol=2)
plt.show()
