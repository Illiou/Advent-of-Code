
with open("input/d1-p1.txt") as h:
    data = [int(line.strip()) for line in h]

data.sort()

goal = 2020


def calc():
    j = len(data) - 1
    for i in range(len(data)):
        diff = goal - data[i]
        while j >= 0:
            if data[j] == diff:
                return data[i] * data[j]
            elif data[j] > diff:
                j -= 1
            else:
                break

print(calc())