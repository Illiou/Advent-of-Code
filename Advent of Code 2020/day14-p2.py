import re
import itertools

mem = {}

with open("input/d14.txt") as f:
    mask = ""
    xes = 0
    for line in f:
        if line[0:4] == "mask":
            mask = line[7:].strip()
            xes = mask.count("X")
        elif line[0:3] == "mem":
            address, value = (int(e) for e in re.match(r"mem\[(\d+)] = (\d+)", line).group(1, 2))
            address_bin = bin(address)[2:]
            address_bin = "0" * (len(mask) - len(address_bin)) + address_bin
            for floating in itertools.product("01", repeat=xes):
                actual_address = []
                floating_iter = iter(floating)
                for i in range(len(mask) - 1, -1, -1):
                    if mask[i] == "X":
                        actual_address.insert(0, next(floating_iter))
                    elif mask[i] == "0":
                        actual_address.insert(0, address_bin[i])
                    elif mask[i] == "1":
                        actual_address.insert(0, "1")
                mem["".join(actual_address)] = value

print(mem)
print(sum(mem.values()))
