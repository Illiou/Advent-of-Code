
with open("input/d8.txt") as f:
    code = f.readlines()
    executed_lines = set()
    current_line = 0
    accumulator = 0
    while current_line not in executed_lines:
        executed_lines.add(current_line)
        op, arg = code[current_line].split()
        if op == "acc":
            accumulator += int(arg)
            current_line += 1
        elif op == "jmp":
            current_line += int(arg)
        else:
            current_line += 1

print(accumulator)
