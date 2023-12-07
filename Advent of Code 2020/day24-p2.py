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

def get_neighbors(pos):
    for direction in direction_mapping.values():
        yield tuple(pos[i] + direction[i] for i in range(len(pos)))

def get_neighbor_sum(pos, tiles):
    return sum(tiles.get(tuple(neighbor), False) for neighbor in get_neighbors(pos))

def get_new_tile_color(tile_color, neighbor_sum):
    if tile_color:
        return not (neighbor_sum == 0 or neighbor_sum > 2)
    else:
        return neighbor_sum == 2

for day in range(100):
    new_tiles = {}
    for pos, tile_color in tiles.items():
        if pos not in new_tiles:
            new_tiles[pos] = get_new_tile_color(tile_color, get_neighbor_sum(pos, tiles))
        for neighbor in get_neighbors(pos):
            if neighbor not in new_tiles:
                new_tiles[neighbor] = get_new_tile_color(tiles.get(neighbor, False), get_neighbor_sum(neighbor, tiles))
    tiles = new_tiles

print(sum(tiles.values()))
