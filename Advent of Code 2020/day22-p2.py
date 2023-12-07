
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

def rec_round(player1, player2):
    previous_hands = set()
    while len(player1) > 0 and len(player2) > 0:
        hands = (tuple(player1), tuple(player2))
        if hands in previous_hands:
            return player1, []
        previous_hands.add(hands)
        p1 = player1.pop(0)
        p2 = player2.pop(0)
        if p1 <= len(player1) and p2 <= len(player2):
            rec_player1, rec_player2 = rec_round(player1[:p1].copy(), player2[:p2].copy())
            if len(rec_player2) == 0:
                player1.append(p1)
                player1.append(p2)
            else:
                player2.append(p2)
                player2.append(p1)
        else:
            if p1 > p2:
                player1.append(p1)
                player1.append(p2)
            else:
                player2.append(p2)
                player2.append(p1)
    return player1, player2

player1, player2 = rec_round(player1, player2)

winner = player2 if player2 else player1
print(sum((i+1) * e for i, e in enumerate(reversed(winner))))
