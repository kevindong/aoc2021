import collections


def read_input(file_name):
    with open(file_name, "r") as f:
        data = f.read()
    data = data.split(",")
    data = list(map(int, data))
    return data


def process(input):
    counts = collections.Counter(input)
    minimum = min(counts)
    maximum = max(counts)
    record = sum(input)
    for i in range(minimum, maximum + 1):
        fuel_cost = 0
        for location, count in counts.items():
            fuel_cost += (max(location, i) - min(location, i)) * count
        record = min(record, fuel_cost)
    return record


data = read_input("input.txt")
print(process(data))
