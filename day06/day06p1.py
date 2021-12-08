def read_input(file_name):
    with open(file_name, "r") as f:
        data = f.readline()
    data = data.split(",")
    data = list(map(int, data))
    return data


def process(initial_state):
    counters = {i: 0 for i in range(9)}
    for state in initial_state:
        counters[state] += 1
    for _ in range(80):
        new_counter = {i: 0 for i in range(9)}
        for day, num in counters.items():
            if day == 0:
                new_counter[8] += num
                new_counter[6] += num
            else:
                new_counter[day - 1] += num
        counters = new_counter
    return sum(counters.values())


data = read_input("input.txt")
print(process(data))
