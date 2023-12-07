
goal = 542529149

with open("input/d9.txt") as f:
    contiguous_set = []
    for line in f:
        number = int(line.strip())
        contiguous_set.append(number)
        while sum(contiguous_set) > goal:
            contiguous_set.pop(0)
        if sum(contiguous_set) == goal:
            break

print(contiguous_set)
print(min(contiguous_set) + max(contiguous_set))
