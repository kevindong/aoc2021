from os import error


def read_input(file_name):
    with open(file_name, "r") as f:
        data = f.read()
    data = data.split("\n")
    return data


def get_pairs():
    return {"(": ")", "[": "]", "{": "}", "<": ">"}


def get_points(c):
    if c == "(":
        return 1
    elif c == "[":
        return 2
    elif c == "{":
        return 3
    elif c == "<":
        return 4
    assert False


def filter_to_incomplete_leftover(lines):
    output = []
    for line in lines:
        stack = []
        is_corrupt = False
        for c in line:
            if c in get_pairs().keys():
                stack.append(c)
            elif c in get_pairs().values():
                if len(stack) == 0:
                    is_corrupt = True
                    break
                last = stack.pop()
                if get_pairs()[last] != c:
                    is_corrupt = True
                    break
        if not is_corrupt and len(stack) != 0:
            output.append(stack)
    return output


def score(line):
    score = 0
    for c in line[::-1]:
        score *= 5
        score += get_points(c)
    return score


lines = read_input("input.txt")
incomplete_lines = filter_to_incomplete_leftover(lines)
points = []
for line in incomplete_lines:
    points.append(score(line))
print(sorted(points)[len(points) // 2])
