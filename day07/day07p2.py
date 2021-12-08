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
    record = None
    for i in range(minimum, maximum + 1):
        fuel_cost = 0
        for location, count in counts.items():
            diff = max(location, i) - min(location, i)
            current_step_cost = (diff * (diff + 1)) // 2
            fuel_cost += current_step_cost * count
        record = min(record or fuel_cost, fuel_cost)
    return record


data = read_input("input.txt")
print(process(data))
