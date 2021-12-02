with open("input.txt", "r") as f:
    data = f.readlines()

x = 0
y = 0
for i in range(len(data)):
    [direction, units] = data[i].split(" ")
    units = int(units)
    if direction == "forward":
        x += units
    elif direction == "up":
        y -= units
    elif direction == "down":
        y += units
    else:
        print("error")
print(x * y)
