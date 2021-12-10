from os import error


def read_input(file_name):
    with open(file_name, "r") as f:
        data = f.read()
    data = data.split("\n")
    return data


def get_pairs():
    return {"(": ")", "[": "]", "{": "}", "<": ">"}


def get_error_score(c):
    if c == ")":
        return 3
    elif c == "]":
        return 57
    elif c == "}":
        return 1197
    elif c == ">":
        return 25137


def process(lines):
    corrupt = 0
    error_score = 0
    for line in lines:
        stack = []
        for c in line:
            if c in get_pairs().keys():
                stack.append(c)
            elif c in get_pairs().values():
                if len(stack) == 0:
                    corrupt += 1
                    error_score += get_error_score(c)
                    break
                last = stack.pop()
                if get_pairs()[last] != c:
                    corrupt += 1
                    error_score += get_error_score(c)
                    break
    return error_score


lines = read_input("input.txt")
corrupt_lines = process(lines)
print(corrupt_lines)
