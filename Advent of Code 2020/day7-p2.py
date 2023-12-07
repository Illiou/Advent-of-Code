import re

children = {}

with open("input/d7.txt") as f:
    for line in f:
        color, content = re.match(r"(.+?) bags contain (.*)\.", line).group(1, 2)
        contents = [(int(child_bag.group(1)), child_bag.group(2)) for child_bag in re.finditer(r"(\d) (.+?)(?= bags?)", content)]
        children[color] = contents

print(children)

def child_rec(bag):
    if not children[bag]:
        return 1
    else:
        return 1 + sum(child_number * child_rec(child_color) for child_number, child_color in children[bag])

bags_required = child_rec("shiny gold") - 1

print(bags_required)
