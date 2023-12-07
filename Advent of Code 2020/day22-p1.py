
player1 = []
player2 = []

with open("input/d22.txt") as f:
    for line in f:
        if line.strip() == "":
            break
        if "Player" in line:
            continue
        player1.append(int(line))

    for line in f:
        if "Player" in line:
            continue
        player2.append(int(line))

while len(player1) > 0 and len(player2) > 0:
    p1 = player1.pop(0)
    p2 = player2.pop(0)
    if p1 > p2:
        player1.append(p1)
        player1.append(p2)
    else:
        player2.append(p2)
        player2.append(p1)

winner = player2 if player2 else player1
print(sum((i+1) * e for i, e in enumerate(reversed(winner))))
