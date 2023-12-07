import numpy as np
import re

problem_file_path = "input/d5.txt"

with open(problem_file_path, "r") as problem_file:
    vent_lines = [tuple(map(int, re.split(r"\D+", line, 3))) for line in problem_file]

vent_count = np.zeros((999, 999), dtype=int)
for x1, y1, x2, y2 in vent_lines:
    mirror = (x1 > x2) ^ (y1 > y2)
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    if x1 != x2 and y1 != y2:
        diagonal = np.eye(x2 - x1 + 1, dtype=int)
        if mirror:
            diagonal = np.fliplr(diagonal)
        vent_count[y1 : y2 + 1, x1 : x2 + 1] += diagonal
    else:
        vent_count[y1 : y2 + 1, x1 : x2 + 1] += 1

print(np.count_nonzero(vent_count > 1))