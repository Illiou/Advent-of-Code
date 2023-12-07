import re

parents = {}

with open("input/d7.txt") as f:
    for line in f:
        color, content = re.match(r"(.+?) bags contain (.*)\.", line).group(1, 2)
        content_colors = re.findall(r"(?<=\d )(.+?)(?= bags?)", content)
        for c in content_colors:
            v = parents.setdefault(c, set())
            v.add(color)

bags_left = ["shiny gold"]
bag_candidates = set()

while len(bags_left) > 0:
    bag = bags_left.pop()
    #bags_left.extend(set(parents[bag]).difference(bag_candidates))
    if bag in parents:
        bags_left.extend(parents[bag])
        bag_candidates.update(parents[bag])

print(len(bag_candidates))
