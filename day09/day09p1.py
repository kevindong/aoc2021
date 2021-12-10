def read_input(file_name):
    with open(file_name, "r") as f:
        data = f.read()
    data = data.split("\n")
    output = []
    for row in data:
        row = list(map(int, list(row)))
        output.append(row)
    return output


def process(grid):
    total_risk_level = 0
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
                total_risk_level += value + 1
    return total_risk_level


grid = read_input("input.txt")
result = process(grid)
print(result)
