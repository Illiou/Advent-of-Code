
count = 0

with open("input/d6.txt") as f:
    yes_set = set()
    first_line = True
    for line in f:
        line = line.strip()
        if line == "":
            count += len(yes_set)
            yes_set = set()
            first_line = True
            continue
        if first_line:
            yes_set.update(line)
            first_line = False
        else:
            yes_set.intersection_update(line)

count += len(yes_set)

print(count)