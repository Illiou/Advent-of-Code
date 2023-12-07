import re


rules = {}

def check_rule(rule, line):
    rule_content = rules[rule]
    if isinstance(rule_content, str):
        if line.startswith(rule_content):
            return line[len(rule_content):]
    else:
        for rule_variants in rule_content:
            reduced_line = line
            for rule in rule_variants:
                reduced_line_again = check_rule(rule, reduced_line)
                if reduced_line_again is not None:
                    reduced_line = reduced_line_again
                else:
                    break
            else:
                return reduced_line


with open("input/d19.txt") as f:
    for line in f:
        line = line.strip()
        if line == "":
            break
        match = re.fullmatch(r"(\d+): \"(\w+)\"", line)
        if match:
            rules[int(match[1])] = match[2]
            continue
        match = re.fullmatch(r"(\d+): (.+)", line)
        if match:
            rules[int(match[1])] = tuple(tuple(int(e) for e in g.split()) for g in match[2].split("|"))
            continue
        raise Exception("no match for line ", line)

    valid_count = 0
    for line in f:
        if check_rule(0, line.strip()) == "":
            valid_count += 1

print(rules)
print(valid_count)
