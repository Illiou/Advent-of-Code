
results = []

def parse_rec(line, start):
    accu = 0
    last_op = None
    i = start
    while i < len(line):
        if line[i] == " ":
            i += 1
            continue
        elif line[i] == "+":
            last_op = int.__add__
        elif line[i] == "*":
            last_op = int.__mul__
        elif line[i] == "(":
            result, end = parse_rec(line, i+1)
            if last_op:
                accu = last_op(accu, result)
            else:
                accu = result
            i = end
        elif line[i] == ")":
            break
        else:
            if last_op:
                accu = last_op(accu, int(line[i]))
            else:
                accu = int(line[i])
        i += 1
    return accu, i


with open("input/d18.txt") as f:
    for line in f:
        results.append(parse_rec(line.strip(), 0)[0])

print(results)
print(sum(results))
