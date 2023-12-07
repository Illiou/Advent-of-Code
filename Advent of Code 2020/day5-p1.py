
seat_id_max = 0
mapping = str.maketrans("FBLR", "0101")

with open("input/d5.txt") as f:
    for line in f:
        line = line.translate(mapping)
        row, col = int(line[:7], 2), int(line[7:], 2)
        seat_id = row * 8 + col
        if seat_id > seat_id_max:
            seat_id_max = seat_id

print(seat_id_max)
