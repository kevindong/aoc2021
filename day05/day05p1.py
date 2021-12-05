from os import read


def read_file(file_name="sample.txt"):
    with open(file_name, "r") as f:
        data = f.readlines()
    transformation = []
    n = 0
    for x in data:
        halves = x.split(" -> ")
        first = halves[0].split(",")
        first = (int(first[0]), int(first[1]))
        second = halves[1].split(",")
        second = (int(second[0]), int(second[1]))
        transformation.append((first, second))
        n = max(n, max(first), max(second))
    return transformation, n + 1


def process(file_name="sample.txt"):
    vents, size = read_file(file_name)
    print(f"Vents: {vents}")
    print(f"Size: {size}")
    grid = [[0 for _ in range(size)] for _ in range(size)]
    for vent in vents:
        dx, dy = get_differential(vent[0], vent[1])
        if (dx, dy) == (0, 0):
            continue
        x1, y1 = vent[0]
        x2, y2 = vent[1]
        while x1 != x2 or y1 != y2:
            grid[x1][y1] += 1
            x1 += dx
            y1 += dy
        grid[x1][y1] += 1
    counter = 0
    print(grid)
    for row in grid:
        for val in row:
            if val > 1:
                counter += 1
    return counter


def get_differential(origin, destination):
    if origin[0] != destination[0] and origin[1] != destination[1]:
        print(f"skipped: {origin} -> {destination}")
        return (0, 0)
    if origin[0] < destination[0]:
        return (1, 0)
    elif origin[0] > destination[0]:
        return (-1, 0)
    elif origin[1] > destination[1]:
        return (0, -1)
    elif origin[1] < destination[1]:
        return (0, 1)
    raise Exception("Should not happen")


print(process("input.txt"))
