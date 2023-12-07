import itertools

with open("input/d9.txt") as f:
    last_25 = []
    for line in f:
        number = int(line.strip())
        if len(last_25) == 25:
            for x, y in itertools.combinations(last_25, 2):
                if x + y == number:
                    break
            else:
                print(number)
            last_25.pop(0)

        last_25.append(number)
