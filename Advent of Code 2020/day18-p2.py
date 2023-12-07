
results = []

def parse_rec(line, start, accu=0, last_op=None):
    break_immediately = last_op is not None
    last_number = 0
    i = start
    while i < len(line):
        if line[i] == " ":
            i += 1
            continue
        elif line[i] == "+":
            result, end = parse_rec(line, i+1, last_number, int.__add__)
            last_number = result
            i = end
        elif line[i] == "*":
            if last_op:
                accu = last_op(accu, last_number)
            else:
                accu = last_number
            last_op = int.__mul__
        elif line[i] == "(":
            result, end = parse_rec(line, i+1)
            last_number = result
            i = end
            if break_immediately:
                break
        elif line[i] == ")":
            break
        else:
            last_number = int(line[i])
            if break_immediately:
                break
        i += 1
    if last_op:
        accu = last_op(accu, last_number)
    else:
        accu = last_number
    return accu, i


with open("input/d18.txt") as f:
    for line in f:
        results.append(parse_rec(line.strip(), 0)[0])

print(results)
print(sum(results))
