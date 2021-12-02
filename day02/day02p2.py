with open("input.txt", "r") as f:
    data = f.readlines()

x = 0
y = 0
aim = 0

for i in range(len(data)):
    [direction, units] = data[i].split(" ")
    units = int(units)
    if direction == "forward":
        x += units
        y += aim * units
    elif direction == "up":
        aim -= units
    elif direction == "down":
        aim += units
    else:
        print("error")
print(x * y)
