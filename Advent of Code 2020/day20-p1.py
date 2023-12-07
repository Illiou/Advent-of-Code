import re
import itertools
from functools import reduce

tile_borders = {}

with open("input/d20.txt") as f:
    lines = iter(f)
    for line in lines:
        tile_id = re.match(r"Tile (\d+):", line).group(1)
        tile = [next(lines).strip() for _ in range(10)]
        tile_borders[int(tile_id)] = {"north": tile[0], "south": tile[-1], "west": "".join([t[0] for t in tile]), "east": "".join([t[-1] for t in tile])}
        next(lines)

print(tile_borders)

# {tile_id: [(direction, other_tile_id, other_direction, reversed)]}
border_matches = {}

for tile, other_tile in itertools.permutations(tile_borders.items(), 2):
    tile_id, borders = tile
    other_tile_id, other_borders = other_tile
    border_matches.setdefault(tile_id, [])
    for direction, border in borders.items():
        border_reversed = "".join(reversed(border))
        for other_direction, other_border in other_borders.items():
            if border == other_border:
                border_matches[tile_id].append((direction, other_tile_id, other_direction, False))
            if border_reversed == other_border:
                border_matches[tile_id].append((direction, other_tile_id, other_direction, True))

print(border_matches)

corner_tiles = [tile for tile, matches in border_matches.items() if len(matches) <= 2]
print(corner_tiles)
print(reduce(lambda a,b: a*b, corner_tiles, 1))
