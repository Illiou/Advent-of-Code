
def run(code):
    executed_lines = []
    current_line = 0
    accumulator = 0
    try:
        while current_line not in executed_lines:
            executed_lines.append(current_line)
            op, arg = code[current_line].split()
            if op == "acc":
                accumulator += int(arg)
                current_line += 1
            elif op == "jmp":
                current_line += int(arg)
            else:
                current_line += 1
    except IndexError:
        pass
    return accumulator, executed_lines


with open("input/d8.txt") as f:
    code = f.readlines()

orig_code = code.copy()
_, orig_executed_lines = run(code)
while True:
    while True:
        line = orig_executed_lines.pop()
        if orig_code[line][0:3] == "jmp":
            code[line] = "nop" + orig_code[line][3:]
            break
        elif orig_code[line][0:3] == "nop":
            code[line] = "jmp" + orig_code[line][3:]
            break

    accumulator, executed_lines = run(code)
    if 626 in executed_lines:
        print(f"Line changed {line}")
        break

    code = orig_code.copy()


print(accumulator)
