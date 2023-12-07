
required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
count = 0

with open("input/d4.txt") as f:
    fields = set()
    for line in f:
        if line.strip() == "":
            if fields.issuperset(required_fields):
                count += 1
            fields = set()
            continue
        for elem in line.strip().split():
            fields.add(elem[0:3])

    if fields.issuperset(required_fields):
        count += 1

print(count)
