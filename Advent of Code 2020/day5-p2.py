
mapping = str.maketrans("FBLR", "0101")
seat_ids = []

with open("input/d5.txt") as f:
    for line in f:
        line = line.translate(mapping)
        row, col = int(line[:7], 2), int(line[7:], 2)
        seat_ids.append(row * 8 + col)

seat_ids.sort()

last = seat_ids[0] - 1
for id in seat_ids:
    if id != (last + 1):
        print(last + 1)
    last = id
