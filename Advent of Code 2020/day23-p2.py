
input = "284573961"
cup_num = 1000000

right_neighbor = [0 for _ in range(len(input))]
for i in range(len(input) - 1):
    right_neighbor[int(input[i]) - 1] = int(input[i + 1])

right_neighbor[int(input[-1]) - 1] = len(input) + 1
right_neighbor.extend(i + 2 for i in range(len(input), cup_num))
right_neighbor[-1] = int(input[0])

current_cup = int(input[0])

for move in range(10000000):
    cup1 = right_neighbor[current_cup - 1]
    cup2 = right_neighbor[cup1 - 1]
    cup3 = right_neighbor[cup2 - 1]
    right_neighbor[current_cup - 1] = right_neighbor[cup3 - 1]

    destination_cup = current_cup - 1 if current_cup > 1 else cup_num
    while destination_cup in [cup1, cup2, cup3]:
        destination_cup = destination_cup - 1 if destination_cup > 1 else cup_num

    right_neighbor[cup3 - 1] = right_neighbor[destination_cup - 1]
    right_neighbor[destination_cup - 1] = cup1
    current_cup = right_neighbor[current_cup - 1]

star1 = right_neighbor[1 - 1]
star2 = right_neighbor[star1 - 1]
print(f"{star1} * {star2} = {star1 * star2}")
