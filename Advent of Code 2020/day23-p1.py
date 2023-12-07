
input = "284573961"

cups = [int(e) for e in input]
max_cup = max(cups)
min_cup = min(cups)

current_cup = cups[0]
for move in range(100):
    cup1 = cups.pop((cups.index(current_cup) + 1) % len(cups))
    cup2 = cups.pop((cups.index(current_cup) + 1) % len(cups))
    cup3 = cups.pop((cups.index(current_cup) + 1) % len(cups))
    destination_cup = current_cup
    while True:
        destination_cup = destination_cup - 1 if destination_cup > min_cup else max_cup
        try:
            destination_cup_pos = cups.index(destination_cup)
            break
        except ValueError:
            pass
    cups.insert((destination_cup_pos + 1) % len(cups), cup1)
    cups.insert((cups.index(destination_cup) + 2) % len(cups), cup2)
    cups.insert((cups.index(destination_cup) + 3) % len(cups), cup3)
    current_cup = cups[(cups.index(current_cup) + 1) % len(cups)]

print(cups)
print("".join(str(cups[(cups.index(1) + c) % len(cups)]) for c in range(1, len(cups))))
