import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

problem_file_path = "input/d9.txt"

with open(problem_file_path, "r") as problem_file:
    heightmap = np.asarray([list(line.strip()) for line in problem_file])

padded_heightmap = np.pad(heightmap, 1, constant_values=9)
print(sliding_window_view(padded_heightmap, (3, 3)))

