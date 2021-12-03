with open("input.txt", "r") as f:
    data = f.readlines()

data = [x.replace("\n", "") for x in data]


def get_counts(x):
    counters = [0 for _ in range(len(x[0]))]
    for point in x:
        for i, c in enumerate(point):
            if c == "1":
                counters[i] += 1
    return counters


def get_o2(data):
    i = 0
    while True:
        if len(data) <= 1:
            return int(data[0], 2)
        counters = get_counts(data)
        if counters[i] * 2 >= len(data):
            data = list(filter(lambda x: x[i] == "1", data))
        else:
            data = list(filter(lambda x: x[i] == "0", data))
        i += 1


def get_co2(data):
    i = 0
    while True:
        if len(data) <= 1:
            return int(data[0], 2)
        counters = get_counts(data)
        if counters[i] * 2 < len(data):
            data = list(filter(lambda x: x[i] == "1", data))
        else:
            data = list(filter(lambda x: x[i] == "0", data))
        i += 1


o2 = get_o2(data)
co2 = get_co2(data)
print(o2 * co2)
