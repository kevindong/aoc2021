def read_input(file_name):
    with open(file_name, "r") as f:
        data = f.read()
    data = data.split("\n")
    data = [x.split(" | ")[1] for x in data]
    data = [x.split(" ") for x in data]
    return data


def process(input):
    counter = {}
    for line in input:
        for display in line:
            l = len(display)
            counter[l] = counter.get(l, 0) + 1
    keys = [2, 4, 3, 7]
    s = 0
    for key in keys:
        s += counter.get(key, 0)
    return s


print(process(read_input("input.txt")))
