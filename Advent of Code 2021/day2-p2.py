problem_file_path = "input/d2.txt"

with open(problem_file_path, "r") as problem_file:
    commands = [(direction, int(amount)) for l in problem_file for direction, amount in [l.split()]]

pos = 0
depth = 0
aim = 0
for direction, amount in commands:
    if direction == "forward":
        pos += amount
        depth += aim * amount
    elif direction == "up":
        aim -= amount
    elif direction == "down":
        aim += amount
    else:
        print("problem")
        break

print(pos, depth, pos*depth)
