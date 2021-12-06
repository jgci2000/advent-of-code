import sys

# part a
if sys.argv[1] == "a":
    data = list()
    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()
            data.append(line)
    
    count = list()
    for i in range(len(data[0])):
        count.append(list())
        for j in range(2):
            count[i].append(list())
            count[i][j] = 0

    for line in data:
        for i, c in enumerate(line):
            if int(c) == 0:
                count[i][0] += 1
            elif int(c) == 1:
                count[i][1] += 1
    
    gamma, epsilon = "", ""
    for i in range(len(count)):
        if count[i][0] > count[i][1]:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
    
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    print(f"power consumption: {gamma * epsilon}")

# part b
if sys.argv[1] == "b":
    data = list()
    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()
            data.append(line)
    
    count = list()
    count.append(list())
    count.append(list())
    oxygen = data.copy()
    new_oxygen = data.copy()

    #oxygen
    for j in range(len(oxygen[0])):
        count[0] = 0; count[1] = 0
        oxygen = new_oxygen.copy()

        for line in oxygen:
            n = int(line[j])
            if n == 0:
                count[0] += 1
            elif n == 1:
                count[1] += 1
        
        if count[0] == count[1]:
            for line in oxygen:
                if int(line[j]) != 1:
                    new_oxygen.remove(line)
        else:
            for line in oxygen: 
                if int(line[j]) != count.index(max(count)):
                    new_oxygen.remove(line)
        if len(new_oxygen) == 1:
            oxygen_rating = int(new_oxygen[0], 2)
            break

    count = list()
    count.append(list())
    count.append(list())
    co2 = data.copy()
    new_co2 = data.copy()

    #co2
    for j in range(len(co2[0])):
        count[0] = 0; count[1] = 0
        co2 = new_co2.copy()

        for line in co2:
            n = int(line[j])
            if n == 0:
                count[0] += 1
            elif n == 1:
                count[1] += 1
        
        if count[0] == count[1]:
            for line in co2:
                if int(line[j]) != 0:
                    new_co2.remove(line)
        else:
            for line in co2: 
                if int(line[j]) != count.index(min(count)):
                    new_co2.remove(line)
        if len(new_co2) == 1:
            co2_rating = int(new_co2[0], 2)
            break

    print(f"result: {co2_rating * oxygen_rating}")


