
pocket_dimension = [[]]

with open("input/d17.txt") as f:
    for line in f:
        pocket_dimension[0].append([1 if e == "#" else 0 for e in line.strip()])

print(pocket_dimension)

neighborhood = [(-1, -1, -1), (0, -1, -1), (1, -1, -1),
                (-1, 0, -1),  (0, 0, -1),  (1, 0, -1),
                (-1, 1, -1),  (0, 1, -1),  (1, 1, -1),

                (-1, -1, 0), (0, -1, 0), (1, -1, 0),
                (-1, 0, 0),              (1, 0,  0),
                (-1, 1, 0),  (0, 1,  0), (1, 1,  0),

                (-1, -1, 1), (0, -1, 1), (1, -1, 1),
                (-1, 0, 1),  (0, 0,  1), (1, 0,  1),
                (-1, 1, 1),  (0, 1,  1), (1, 1,  1)]

for cycle in range(6):
    new_pocket_dimension = []
    for z in range(len(pocket_dimension) + 2):
        new_pocket_dimension.append([])
        for y in range(len(pocket_dimension[0]) + 2):
            new_pocket_dimension[z].append([])
            for x in range(len(pocket_dimension[0][0]) + 2):
                active_neighbors = sum(pocket_dimension[z+k-1][y+j-1][x+i-1] for i, j, k in neighborhood
                                       if 0 <= z+k-1 < len(pocket_dimension) and 0 <= y+j-1 < len(pocket_dimension[0]) and 0 <= x+i-1 < len(pocket_dimension[0][0]))
                # if active
                if 0 <= z-1 < len(pocket_dimension) and 0 <= y-1 < len(pocket_dimension[0]) and 0 <= x-1 < len(pocket_dimension[0][0]) and \
                        pocket_dimension[z-1][y-1][x-1]:
                    if 2 <= active_neighbors <= 3:
                        new_pocket_dimension[z][y].append(1)
                    else:
                        new_pocket_dimension[z][y].append(0)
                # inactive
                else:
                    if active_neighbors == 3:
                        new_pocket_dimension[z][y].append(1)
                    else:
                        new_pocket_dimension[z][y].append(0)
    pocket_dimension = new_pocket_dimension
    print(pocket_dimension)

print(sum(sum(sum(j) for j in k) for k in pocket_dimension))
