import sys

# part a
if sys.argv[1] == "a":
    x, z = 0, 0
    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip().split()
            if line[0] == "forward":
                x += int(line[1])
            elif line[0] == "down":
                z += int(line[1])
            elif line[0] == "up":
                z += - int(line[1])
                
    print(f"(x, z) = ({x}, {z})")
    print(f"result: {x * z}")

# part b
if sys.argv[1] == "b":
    aim, x, z = 0, 0, 0
    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip().split()
            if line[0] == "forward":
                x += int(line[1])
                z += int(line[1]) * aim
            elif line[0] == "down":
                aim += int(line[1])
            elif line[0] == "up":
                aim += - int(line[1])
                
    print(f"(x, z, aim) = ({x}, {z}, {aim})")
    print(f"result: {x * z}")
