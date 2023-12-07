import re

problem_file = "input/day5.txt"

with open(problem_file) as file:
    input_lines = file.readlines()

empty_line_index = input_lines.index("\n")
stacks_list = input_lines[:empty_line_index - 1]
rearr_list = input_lines[empty_line_index + 1:]

stacks = []
i = 1
while True:
    stacks.append([])
    for line in reversed(stacks_list):
        elem = line[i]
        if elem != " ":
            stacks[-1].append(elem)
    i += 4
    if i >= len(stacks_list[0]):
        break

# stacks = [[elem for i in range(len(stacks_list)) if (elem := stacks_list[i][row]) != " "] for row in range(1, len(stacks_list[0]), 4)]

regex = re.compile(r".*?(\d+).*?(\d+).*?(\d+)")
for line in rearr_list:
    count, from_, to = map(lambda x: int(x), regex.match(line).group(1, 2, 3))
    stacks[to-1] += reversed(stacks[from_-1][-count:])
    del stacks[from_-1][-count:]

print(stacks)
print("".join(l[-1] for l in stacks))
