import re

valid_count = 0

with open("input/d2-p2.txt") as f:
    for line in f:
        reg = re.match(r"(\d+)-(\d+) ([a-z]): ([a-z]+)", line.strip())
        pos1, pos2, letter, password = int(reg[1]) - 1, int(reg[2]) - 1, reg[3], reg[4]
        if (password[pos1] == letter) != (password[pos2] == letter):
            valid_count += 1

print(valid_count)