
filename = "input.txt"
if filename == "input_test.txt":
    x = 10
else:
    x = 1000

clouds = list()

with open(filename, "r") as file:
    for line in file:
        line = line.strip().split(" -> ")
        line[0] = line[0].split(",")
        line[1] = line[1].split(",")
        line[0] = [int(c) for c in line[0]]
        line[1] = [int(c) for c in line[1]]
        clouds.append((tuple(line[0]), tuple(line[1])))

rm = list()
for point in clouds:
    if point[0][0] != point[1][0] and point[0][1] != point[1][1]:
        rm.append(point)
clouds_diag = list()
for point in rm:
    clouds.remove(point)
    clouds_diag.append(point)

dia_size = x
diagram = list()
for i in range(dia_size):
    diagram.append(list())
    for j in range(dia_size):
        diagram[i].append(0)

for point in clouds: 
    org_x, org_y = point[0]
    steps_x = point[1][0] - point[0][0]
    steps_y = point[1][1] - point[0][1]

    if steps_x < 0:
        for i in range(abs(steps_x) + 1):
            diagram[org_y][org_x - i] += 1
    elif steps_x > 0:
        for i in range(abs(steps_x) + 1):
            diagram[org_y][org_x + i] += 1

    if steps_y < 0:
        for i in range(abs(steps_y) + 1):
            diagram[org_y - i][org_x] += 1
    elif steps_y > 0:
        for i in range(abs(steps_y) + 1):
            diagram[org_y + i][org_x] += 1

count = 0
for i in range(dia_size):
    for j in range(dia_size):
        if diagram[i][j] >= 2:
            count += 1
print(f"count part_a: {count}")

for point in clouds_diag:
    org_x, org_y = point[0]
    steps_x = point[1][0] - point[0][0]
    steps_y = point[1][1] - point[0][1]
    
    if steps_x < 0 and steps_y < 0:
        for i in range(abs(steps_x) + 1):
            diagram[org_y - i][org_x - i] += 1
    if steps_x > 0 and steps_y < 0:
        for i in range(abs(steps_x) + 1):
            diagram[org_y - i][org_x + i] += 1
    if steps_x < 0 and steps_y > 0:
        for i in range(abs(steps_x) + 1):
            diagram[org_y + i][org_x - i] += 1
    if steps_x > 0 and steps_y > 0:
        for i in range(abs(steps_x) + 1):
            diagram[org_y + i][org_x + i] += 1

count = 0
for i in range(dia_size):
    for j in range(dia_size):
        if diagram[i][j] >= 2:
            count += 1
print(f"count part_b: {count}")






