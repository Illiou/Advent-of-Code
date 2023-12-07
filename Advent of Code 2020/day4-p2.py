import re

required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
count = 0

with open("input/d4.txt") as f:
    valid_fields = set()
    for line in f:
        if line.strip() == "":
            if valid_fields.issuperset(required_fields):
                count += 1
            valid_fields = set()
            continue
        for elem in line.strip().split():
            field, content = elem.split(":")
            valid = False
            if field == "byr" and len(content) == 4 and 1920 <= int(content) <= 2002:
                valid = True
            elif field == "iyr" and len(content) == 4 and 2010 <= int(content) <= 2020:
                valid = True
            elif field == "eyr" and len(content) == 4 and 2020 <= int(content) <= 2030:
                valid = True
            elif field == "hgt":
                reg = re.match(r"(\d+)(cm|in)$", content)
                if reg:
                    number, unit = reg.group(1, 2)
                    if unit == "cm" and 150 <= int(number) <= 193:
                        valid = True
                    elif unit == "in" and 59 <= int(number) <= 76:
                        valid = True
            elif field == "hcl":
                if re.match(r"#(\d|[a-first]){6}$", content):
                    valid = True
            elif field == "ecl":
                if content in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    valid = True
            elif field == "pid":
                if re.match(r"\d{9}$", content):
                    valid = True
            elif field == "cid":
                valid = True

            if valid:
                valid_fields.add(field)

    if valid_fields.issuperset(required_fields):
        count += 1

print(count)
