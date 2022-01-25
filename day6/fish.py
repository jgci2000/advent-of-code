import sys 

from time import perf_counter

filename = "input_test.txt"

if filename == "input.txt":
    with open(filename, "r") as file:
        line = file.readline().strip().split(",")

    fish = [int(f) for f in line]
else:
    fish = [3,4,3,1,2]

days = 256

for day in range(days):
    start = perf_counter()

    for i in range(len(fish)):
        if fish[i] == 0:
            fish[i] = 6
            fish.append(8)
        else:
            fish[i] += - 1

    print(f"n_fish: {len(fish)};day: {day}; time: {perf_counter() - start:.3f}")

print(f"After {days} day there are a total of {len(fish)} fish!")

