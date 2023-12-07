import re
import itertools
import math

tile_borders = {}
tiles = {}

with open("input/d20.txt") as f:
    lines = iter(f)
    for line in lines:
        tile_id = int(re.match(r"Tile (\d+):", line).group(1))
        tile = [next(lines).strip() for _ in range(10)]
        tiles[tile_id] = tile
        tile_borders[tile_id] = {"north": tile[0], "south": tile[-1][::-1], "west": "".join([t[0] for t in tile[::-1]]), "east": "".join([t[-1] for t in tile])}
        next(lines)

# {tile_id: [{direction: [other_tile_id, other_direction, reversed]]}
border_matches = {}

for tile, other_tile in itertools.permutations(tile_borders.items(), 2):
    tile_id, borders = tile
    other_tile_id, other_borders = other_tile
    border_matches.setdefault(tile_id, {})
    for direction, border in borders.items():
        border_reversed = "".join(reversed(border))
        for other_direction, other_border in other_borders.items():
            if border == other_border:
                border_matches[tile_id][direction] = [other_tile_id, other_direction, False]
            if border_reversed == other_border:
                border_matches[tile_id][direction] = [other_tile_id, other_direction, True]

print(border_matches)


corner_tiles = [(tile, matches) for tile, matches in border_matches.items() if len(matches) <= 2]

print(corner_tiles)

def mirror_horizontal(array):
    return [l[::-1] for l in array]

def mirror_vertical(array):
    return array[::-1]

def turn_right(array):
    return ["".join(array[j][i] for j in range(len(array)-1, -1, -1)) for i in range(len(array))]

def turn_left(array):
    return ["".join(array[j][i] for j in range(len(array))) for i in range(len(array)-1, -1, -1)]

def turn_halfway(array):
    return [l[::-1] for l in array][::-1]


tiles_by_side = int(math.sqrt(len(tiles)))
tile_size = len(tiles[corner_tiles[0][0]])
# [[(tile_id, tile),...],...]
tile_arrangement = [[(corner_tiles[0][0], tiles[corner_tiles[0][0]])]]


direction_order = ["north", "east", "south", "west"]
direction_mirror_vertical = {"north": "south", "south": "north", "east": "east", "west": "west"}
direction_mirror_horizontal = {"east": "west", "west": "east", "north": "north", "south": "south"}

for i in range(1, tiles_by_side):
    tile_arrangement.append([])
    next_tile_id, next_tile_direction, next_tile_mirror = border_matches[tile_arrangement[i - 1][0][0]]["south"]
    next_tile = tiles[next_tile_id]
    if next_tile_direction == "east":
        border_matches[next_tile_id] = {direction_order[(direction_order.index(direction) - 1) % 4]: border
                                        for direction, border in border_matches[next_tile_id].items()}
        if not next_tile_mirror:
            border_matches[next_tile_id] = {direction_mirror_horizontal[direction]: border
                                            for direction, border in border_matches[next_tile_id].items()}
            for direction in direction_order:
                try:
                    border_matches[next_tile_id][direction][2] ^= True
                except KeyError:
                    pass
            next_tile = mirror_horizontal(turn_left(next_tile))
        else:
            next_tile = turn_left(next_tile)
    elif next_tile_direction == "south":
        border_matches[next_tile_id] = {direction_order[(direction_order.index(direction) + 2) % 4]: border
                                        for direction, border in border_matches[next_tile_id].items()}
        if not next_tile_mirror:
            border_matches[next_tile_id] = {direction_mirror_horizontal[direction]: border
                                            for direction, border in border_matches[next_tile_id].items()}
            for direction in direction_order:
                try:
                    border_matches[next_tile_id][direction][2] ^= True
                except KeyError:
                    pass
            next_tile = mirror_vertical(next_tile)
        else:
            next_tile = turn_halfway(next_tile)
    elif next_tile_direction == "west":
        border_matches[next_tile_id] = {direction_order[(direction_order.index(direction) + 1) % 4]: border
                                        for direction, border in border_matches[next_tile_id].items()}
        if not next_tile_mirror:
            border_matches[next_tile_id] = {direction_mirror_horizontal[direction]: border
                                            for direction, border in border_matches[next_tile_id].items()}
            for direction in direction_order:
                try:
                    border_matches[next_tile_id][direction][2] ^= True
                except KeyError:
                    pass
            next_tile = mirror_horizontal(turn_right(next_tile))
        else:
            next_tile = turn_right(next_tile)
    else:
        if not next_tile_mirror:
            border_matches[next_tile_id] = {direction_mirror_horizontal[direction]: border
                                            for direction, border in border_matches[next_tile_id].items()}
            for direction in direction_order:
                try:
                    border_matches[next_tile_id][direction][2] ^= True
                except KeyError:
                    pass
            next_tile = mirror_horizontal(next_tile)
    tile_arrangement[i].append((next_tile_id, next_tile))


for i in range(tiles_by_side):
    for j in range(1, tiles_by_side):
        next_tile_id, next_tile_direction, next_tile_mirror = border_matches[tile_arrangement[i][j - 1][0]]["east"]
        next_tile = tiles[next_tile_id]
        if next_tile_direction == "north":
            border_matches[next_tile_id] = {direction_order[(direction_order.index(direction) - 1) % 4]: border
                                            for direction, border in border_matches[next_tile_id].items()}
            if not next_tile_mirror:
                border_matches[next_tile_id] = {direction_mirror_vertical[direction]: border
                                                for direction, border in border_matches[next_tile_id].items()}
                for direction in direction_order:
                    try:
                        border_matches[next_tile_id][direction][2] ^= True
                    except KeyError:
                        pass
                next_tile = mirror_vertical(turn_left(next_tile))
            else:
                next_tile = turn_left(next_tile)
        elif next_tile_direction == "east":
            border_matches[next_tile_id] = {direction_order[(direction_order.index(direction) + 2) % 4]: border
                                            for direction, border in border_matches[next_tile_id].items()}
            if not next_tile_mirror:
                border_matches[next_tile_id] = {direction_mirror_vertical[direction]: border
                                                for direction, border in border_matches[next_tile_id].items()}
                for direction in direction_order:
                    try:
                        border_matches[next_tile_id][direction][2] ^= True
                    except KeyError:
                        pass
                next_tile = mirror_horizontal(next_tile)
            else:
                next_tile = turn_halfway(next_tile)
        elif next_tile_direction == "south":
            border_matches[next_tile_id] = {direction_order[(direction_order.index(direction) + 1) % 4]: border
                                            for direction, border in border_matches[next_tile_id].items()}
            if not next_tile_mirror:
                border_matches[next_tile_id] = {direction_mirror_vertical[direction]: border
                                                for direction, border in border_matches[next_tile_id].items()}
                for direction in direction_order:
                    try:
                        border_matches[next_tile_id][direction][2] ^= True
                    except KeyError:
                        pass
                next_tile = mirror_vertical(turn_right(next_tile))
            else:
                next_tile = turn_right(next_tile)
        else:
            if not next_tile_mirror:
                border_matches[next_tile_id] = {direction_mirror_vertical[direction]: border
                                                for direction, border in border_matches[next_tile_id].items()}
                for direction in direction_order:
                    try:
                        border_matches[next_tile_id][direction][2] ^= True
                    except KeyError:
                        pass
                next_tile = mirror_vertical(next_tile)
        tile_arrangement[i].append((next_tile_id, next_tile))

# for line in tile_arrangement:
#     for i in range(tile_size):
#         print(" ".join(line[j][1][i] for j in range(tiles_by_side)))
#     print()


def remove_border(array):
    return [array[i][1:-1] for i in range(1, len(array) - 1)]

image_tiles = []

for line in tile_arrangement:
    image_tiles.append([])
    for _, tile in line:
        image_tiles[-1].append(remove_border(tile))

image = []

for line in image_tiles:
    for i in range(tile_size-2):
        image.append("".join(line[j][i] for j in range(tiles_by_side)))

for line in image:
    print(line)

seamonster1 = r"(?=..................#.)"
seamonster2 = r"(?=#....##....##....###)"
seamonster3 = r"(?=.#..#..#..#..#..#...)"

seamonster_parts = seamonster1.count("#") + seamonster2.count("#") + seamonster3.count("#")

image_width = len(image[0]) + 1

for _ in range(2):
    for _ in range(4):
        image_string = "\n".join(image)
        seamonster1_matches = [match.start() for match in re.finditer(seamonster1, image_string)]
        seamonster2_matches = [match.start() for match in re.finditer(seamonster2, image_string)]
        seamonster3_matches = [match.start() for match in re.finditer(seamonster3, image_string)]
        actual_matches = [pos for pos in seamonster1_matches if pos + image_width in seamonster2_matches and pos + (image_width * 2) in seamonster3_matches]
        if actual_matches:
            print(actual_matches)
            print(image_string.count("#") - len(actual_matches) * seamonster_parts)
        image = turn_right(image)
    image = mirror_horizontal(image)
