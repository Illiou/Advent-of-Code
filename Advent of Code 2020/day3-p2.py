import numpy as np
from functools import reduce

map_ = np.genfromtxt("input/d3.txt", dtype=str, comments=None, delimiter=1)

tree_counts = []
width = map_.shape[1]

for x_diff, y_diff in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    x = 0
    y = 0
    tree_count = 0
    while y < map_.shape[0]:
        if map_[y, x] == "#":
            tree_count += 1
        x = (x + x_diff) % width
        y += y_diff
    tree_counts.append(tree_count)

print(reduce(lambda a, b: a*b, tree_counts, 1))