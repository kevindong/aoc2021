with open("input.txt", "r") as f:
    data = f.readlines()

data = [int(i) for i in data]

increasing = 0
for i in range(1, len(data)):
    if data[i] > data[i - 1]:
        increasing += 1

print(increasing)
