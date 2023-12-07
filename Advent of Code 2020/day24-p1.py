import re

tiles = {}

direction_mapping = {"e": (1, 0), "se": (0.5, 1), "sw": (-0.5, 1), "w": (-1, 0), "nw": (-0.5, -1), "ne": (0.5, -1)}

with open("input/d24.txt") as f:
    for line in f:
        current_tile = [0, 0]
        for match in re.finditer(r"(se|sw|nw|ne|e|w)", line.strip()):
            d = direction_mapping[match[0]]
            current_tile = [current_tile[i] + d[i] for i in range(len(current_tile))]
        old = tiles.get(tuple(current_tile), False)
        tiles[tuple(current_tile)] = old ^ True

print(tiles)
print(sum(tiles.values()))
