import sys

# part a
if sys.argv[1] == "a":
    increased = 0
    with open("input.txt", "r") as file:
        old_depth = int(file.readline().strip())
        for line in file:
            depth = int(line.strip())
            if old_depth < depth:
                increased += 1
            old_depth = depth

    print(f"increased {increased} times")

# part b
if sys.argv[1] == "b":
    increased = 0
    data = list()
    window = list()
    with open("input.txt", "r") as file:
        for line in file:
            data.append(int(line.strip()))

    for i in range(len(data)):
        s = 0
        for j in range(3):
            if i + j < len(data):
                s += data[i + j]
        window.append(s)
        if i != 0:
            if window[i - 1] < window[i]:
                increased += 1
    
    print(f"increased {increased} times")


