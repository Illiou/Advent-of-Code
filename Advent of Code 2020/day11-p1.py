
seat_map = []

with open("input/d11.txt") as f:
    for line in f:
        seat_map.append(list(line.strip()))


OCCUPIED = "#"
EMPTY = "L"
FLOOR = "."

height = len(seat_map)
width = len(seat_map[0])

neighborhood = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
changed = True
it = 0
while changed:
    print(it)
    it += 1
    changed = False
    new_seat_map = []
    for i in range(height):
        new_seat_map.append([])
        for j in range(width):
            seat = seat_map[i][j]
            occupied_neighborhood_count = sum(seat_map[i+y][j+x] == OCCUPIED for x, y in neighborhood if 0 <= j+x < width and 0 <= i+y < height)
            if occupied_neighborhood_count >= 4 and seat == OCCUPIED:
                new_seat_map[i].append(EMPTY)
                changed = True
                continue
            if occupied_neighborhood_count == 0 and seat == EMPTY:
                new_seat_map[i].append(OCCUPIED)
                changed = True
                continue
            new_seat_map[i].append(seat)
    seat_map = new_seat_map

for line in seat_map:
    print("".join(line))

print(sum(line.count(OCCUPIED) for line in seat_map))