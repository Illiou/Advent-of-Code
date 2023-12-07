import numpy as np

problem_file_path = "input/d6.txt"

fish = np.zeros((26984457539), dtype=np.byte)
with open(problem_file_path, "r") as problem_file:
    for i, e in enumerate(problem_file.readline().split(",")):
        fish[i] = e

active_fish = np.count_nonzero()
for day in range(256):
    print(day)
    fish -= 1
    end_cycle = fish < 0
    fish[end_cycle] = 6
    fish[active_fish : active_fish + np.count_nonzero(end_cycle)] = 8
    active_fish += np.count_nonzero(end_cycle)

print(len(fish))