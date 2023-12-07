import re

mem = {}

with open("input/d14.txt") as f:
    mask_or = 0
    mask_and = 0b111111111111111111111111111111111111
    for line in f:
        if line[0:4] == "mask":
            mask = line[7:].strip()
            mask_or = int(mask.replace("X", "0"), 2)
            mask_and = int(mask.replace("X", "1"), 2)
        elif line[0:3] == "mem":
            address, value = (int(e) for e in re.match(r"mem\[(\d+)] = (\d+)", line).group(1, 2))
            value = (value | mask_or) & mask_and
            mem[address] = value

print(mem)
print(sum(mem.values()))
