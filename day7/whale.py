import sys
import math

pos = list()

filename = "input.txt"
with open(filename, "r") as file:
    line = file.readline().strip().split(",")
    pos = [int(p) for p in line]

max_pos = max(pos)
prev_cost = 1e100
best_pos = 0

broken = False

cost_per_step = 2

for i in range(max_pos):
    curr_cost = 0
    for p in pos:
        steps = abs(p - i)
        curr_cost += steps * (steps + 1) / 2

        if curr_cost >= prev_cost:
            broken = True
            break
        broken = False
    
    if not broken:
        prev_cost = curr_cost
        best_pos = i

print(f"best_pos: {best_pos}; fuel_cost: {prev_cost}")



