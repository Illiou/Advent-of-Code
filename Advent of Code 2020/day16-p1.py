import re

fields = {}
tickets = []

with open("input/d16.txt") as f:
    for line in f:
        if line.strip() == "":
            break
        field, f1, t1, f2, t2 = re.match("([\w\s]+): (\d+)-(\d+) or (\d+)-(\d+)", line).group(1, 2, 3, 4, 5)
        fields[field] = (range(int(f1), int(t1)+1), range(int(f2), int(t2)+1))
    for line in f:
        if line.strip() == "":
            break
    for line in f:
        if line.strip() == "nearby tickets:":
            continue
        tickets.append([int(e) for e in line.strip().split(",")])

print(fields)
print(tickets)

error_rate = 0

for ticket in tickets:
    for value in ticket:
        for field in fields.values():
            for range_ in field:
                if value in range_:
                    break
            else:
                continue
            break
        else:
            error_rate += value

print(error_rate)