
x, y = 0, 0

with open("input/d12.txt") as f:
    direction = 0
    direction_mapping = {0: (1, 0), 90: (0, 1), 180: (-1, 0), 270: (0, -1)}
    for line in f:
        action, value = line[0], int(line[1:])
        if action == "N":
            y -= value
        elif action == "E":
            x += value
        elif action == "S":
            y += value
        elif action == "W":
            x -= value
        elif action == "L":
            direction = (direction + (360 - value)) % 360
        elif action == "R":
            direction = (direction + value) % 360
        elif action == "F":
            x_fac, y_fac = direction_mapping[direction]
            x += x_fac * value
            y += y_fac * value

print(abs(x) + abs(y))