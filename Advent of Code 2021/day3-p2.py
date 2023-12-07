problem_file_path = "input/d3.txt"

with open(problem_file_path, "r") as problem_file:
    numbers = [l.strip() for l in problem_file]

def split_by_most_common(l, pos):
    a = []
    b = []
    for e in l:
        if e[pos] == "1":
            a.append(e)
        else:
            b.append(e)
    if len(a) < len(b):
        a, b = b, a
    return a, b

oxygen, co2 = split_by_most_common(numbers, 0)

for pos in range(1, len(numbers[0])):
    oxygen, _ = split_by_most_common(oxygen, pos)
    if len(oxygen) == 1:
        break
oxygen = oxygen[0]

for pos in range(1, len(numbers[0])):
    _, co2 = split_by_most_common(co2, pos)
    if len(co2) == 1:
        break
co2 = co2[0]


print(oxygen, co2, int(oxygen, 2) * int(co2, 2))
