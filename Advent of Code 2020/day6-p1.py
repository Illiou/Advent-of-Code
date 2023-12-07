
count = 0

with open("input/d6.txt") as f:
    yes_set = set()
    for line in f:
        line = line.strip()
        if line == "":
            count += len(yes_set)
            yes_set = set()
            continue
        yes_set.update(line)

if yes_set != set():
    count += len(yes_set)

print(count)