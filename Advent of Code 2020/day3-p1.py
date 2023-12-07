import numpy as np

map = np.genfromtxt("input/d3.txt", dtype=str, comments=None, delimiter=1)

tree_count = 0
x = 0
y = 0
width = map.shape[1]

while y < map.shape[0]:
    if map[y, x] == "#":
        tree_count += 1
    x = (x + 3) % width
    y += 1

print(tree_count)