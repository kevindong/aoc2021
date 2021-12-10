def read_input(file_name):
    with open(file_name, "r") as f:
        data = f.read()
    data = data.split("\n")
    output = []
    for row in data:
        row = list(map(int, list(row)))
        output.append(row)
    return output


def find_low_points(grid):
    low_points = []
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            neighbors = []
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for direction in directions:
                x = i + direction[0]
                y = j + direction[1]
                if 0 <= x < len(grid) and 0 <= y < len(row):
                    neighbors.append(grid[x][y])
            if all(value < neighbor for neighbor in neighbors):
                low_points.append((i, j))
    return low_points


def process(grid, low_points):
    sizes = []
    for low_point in low_points:
        sizes.append(dfs_fill(grid, low_point[0], low_point[1]))
    sizes.sort()
    return sizes[-1] * sizes[-2] * sizes[-3]


def dfs_fill(grid, i, j):
    if not (0 <= i < len(grid)) or not (0 <= j < len(grid[i])):
        return 0
    elif grid[i][j] == 9:
        return 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    sum = 1
    grid[i][j] = 9
    for direction in directions:
        sum += dfs_fill(grid, i + direction[0], j + direction[1])
    return sum


grid = read_input("input.txt")
low_points = find_low_points(grid)
result = process(grid, low_points)
print(result)
