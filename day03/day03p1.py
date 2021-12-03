with open("input.txt", "r") as f:
    data = f.readlines()

data = [x.replace("\n", "") for x in data]

input_size = len(data)

counters = [0 for i in range(len(data[0]))]

for point in data:
    for i, c in enumerate(point):
        if c == "1":
            counters[i] += 1

majority = []
for i, point in enumerate(counters):
    if point > (input_size) // 2:
        majority.append("1")
    else:
        majority.append("0")

gamma = "".join(majority)
gamma = int(gamma, 2)

translate = ""
for c in "".join(majority):
    if c == "1":
        translate += "0"
    else:
        translate += "1"
epsilon = int(translate, 2)

print(gamma * epsilon)
