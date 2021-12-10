def read_input(file_name):
    with open(file_name, "r") as f:
        data = f.read()
    data = data.split("\n")
    output = []

    for d in data:
        d = d.replace(" | ", " ")
        d = d.split(" ")
        d = ["".join(sorted(x)) for x in d]
        output.append(d)
    return output


def process(entries):
    sum = 0
    for i, entry in enumerate(entries):
        mapping = find_mapping(entry)
        s = ""
        for c in entry[-4:]:
            s += str(mapping[c])
        s = int(s)
        sum += s
    return sum


def find_mapping(entry):
    # print(entry)
    mapping = {}
    len_to_num_mapping = {2: 1, 4: 4, 3: 7, 7: 8}
    proper_to_actual_mapping = {}
    actual_to_proper_mapping = {}
    for i in entry[:10]:
        if len(i) not in len_to_num_mapping:
            continue
        mapping[i] = len_to_num_mapping[len(i)]
        mapping[len_to_num_mapping[len(i)]] = i

    actual_a = "".join(sorted(set(mapping[7]) - set(mapping[1])))
    proper_to_actual_mapping["a"] = actual_a
    actual_to_proper_mapping[actual_a] = "a"

    len_six = list(filter(lambda x: len(x) == 6, entry[:10]))
    six = None
    for c in len_six:
        one = mapping[1]
        if all(x in c for x in one):
            continue
        else:
            six = c
            break
    mapping[6] = six
    mapping[six] = 6
    len_six.remove(six)

    four = mapping[4]
    first = len_six[0]
    second = len_six[1]
    if all(x in first for x in four):
        mapping[9] = first
        mapping[first] = 9
        mapping[0] = second
        mapping[second] = 0
    else:
        mapping[9] = second
        mapping[second] = 9
        mapping[0] = first
        mapping[first] = 0

    six = mapping[6]
    len_fives = list(filter(lambda x: len(x) == 5, entry[:10]))
    five = None
    for candidate in len_fives:
        found = True
        for segment in candidate:
            if segment not in six:
                found = False
                break
        if found:
            five = candidate
            break
    mapping[5] = five
    mapping[five] = 5

    e = list(set(mapping[6]) - set(mapping[5]))[0]
    proper_to_actual_mapping["e"] = e
    actual_to_proper_mapping[e] = "e"

    len_fives.remove(mapping[5])
    if e in len_fives[0]:
        mapping[2] = len_fives[0]
        mapping[len_fives[0]] = 2
        mapping[3] = len_fives[1]
        mapping[len_fives[1]] = 3
    else:
        mapping[2] = len_fives[1]
        mapping[len_fives[1]] = 2
        mapping[3] = len_fives[0]
        mapping[len_fives[0]] = 3

    for k in mapping.keys():
        if isinstance(k, int):
            continue
        if sorted(k) != list(k):
            print(f"problem: {k}")

    return mapping


print(process(read_input("input.txt")))
