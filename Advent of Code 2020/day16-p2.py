import re

fields = {}
tickets = []
my_ticket = None

with open("input/d16.txt") as f:
    for line in f:
        if line.strip() == "":
            break
        field, f1, t1, f2, t2 = re.match("([\w\s]+): (\d+)-(\d+) or (\d+)-(\d+)", line).group(1, 2, 3, 4, 5)
        fields[field] = (range(int(f1), int(t1)+1), range(int(f2), int(t2)+1))
    for line in f:
        if line.strip() == "":
            break
        if line.strip() == "your ticket:":
            continue
        my_ticket = [int(e) for e in line.strip().split(",")]
    for line in f:
        if line.strip() == "nearby tickets:":
            continue
        tickets.append([int(e) for e in line.strip().split(",")])

print(fields)
print(tickets)
print(my_ticket)

invalid_ticket_ids = []
for i, ticket in enumerate(tickets):
    for value in ticket:
        for field in fields.values():
            for range_ in field:
                if value in range_:
                    break
            else:
                continue
            break
        else:
            invalid_ticket_ids.append(i)
            break

print(invalid_ticket_ids)

valid_tickets = [t for i, t in enumerate(tickets) if i not in invalid_ticket_ids]
print(valid_tickets)


field_positions = {field: [] for field in fields}

# evil fucking nested loop
for i in range(len(my_ticket)):
    for field_name, field in fields.items():
        for ticket in valid_tickets:
            for range_ in field:
                if ticket[i] in range_:
                    break
            else:
                break
        else:
            field_positions[field_name].append(i)

print(field_positions)

while True:
    position_naked_singles = []
    for positions in field_positions.values():
        if len(positions) == 1:
            position_naked_singles.append(positions[0])
    for position in position_naked_singles:
        for field, positions in field_positions.items():
            if len(positions) != 1:
                try:
                    positions.remove(position)
                except ValueError:
                    pass

    # position_hidden_singles = [0 for _ in range(len(my_ticket))]
    # for positions in field_positions.values():
    #     for position in positions:
    #         position_hidden_singles[position] += 1
    # for position in position_hidden_singles:
    #     if position == 1:
    #         for field in field_positions:
    #             try:
    #                 field_positions[field].remove(position)
    #             except ValueError:
    #                 pass

    print(field_positions)

    if sum(len(pos) for pos in field_positions.values()) <= len(my_ticket):
        break

departure_fields = [pos[0] for field, pos in field_positions.items() if "departure" in field]

product = 1
for i in departure_fields:
    product *= my_ticket[i]

print(product)
