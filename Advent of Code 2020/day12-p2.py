
x, y = 0, 0
x_way, y_way = 10, -1

with open("input/d12.txt") as f:
    rotation_mapping = {90: (0, -1, 1, 0), 180: (-1, 0, 0, -1), 270: (0, 1, -1, 0)}
    for line in f:
        action, value = line[0], int(line[1:])
        if action == "N":
            y_way -= value
        elif action == "E":
            x_way += value
        elif action == "S":
            y_way += value
        elif action == "W":
            x_way -= value
        elif action == "L":
            x_x, y_x, x_y, y_y = rotation_mapping[360 - value]
            x_way, y_way = x_x * x_way + y_x * y_way, x_y * x_way + y_y * y_way
        elif action == "R":
            x_x, y_x, x_y, y_y = rotation_mapping[value]
            x_way, y_way = x_x * x_way + y_x * y_way, x_y * x_way + y_y * y_way
        elif action == "F":
            x += x_way * value
            y += y_way * value

print(abs(x) + abs(y))