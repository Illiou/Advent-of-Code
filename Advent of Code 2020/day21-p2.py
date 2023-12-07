import re
import itertools
from operator import itemgetter

ingredients = []
allergens = []

with open("input/d21.txt") as f:
    for line in f:
        ing, aller = re.search(r"(.*) \(contains (.*)\)", line).group(1, 2)
        ingredients.append(set(ing.split()))
        allergens.append(set(aller.split(", ")))

all_allergens = set.union(*allergens)
all_ingredients = set.union(*ingredients)
ingredient_allergens = {ing: all_allergens.copy() for ing in all_ingredients}

for a, b in itertools.combinations(range(len(ingredients)), 2):
    common_allergens = allergens[a] & allergens[b]
    uncommon_ingredients = ingredients[a] ^ ingredients[b]
    for uncommon_ingredient in uncommon_ingredients:
        ingredient_allergens[uncommon_ingredient] -= common_allergens

for allergen in all_allergens:
    common_ingredients = all_ingredients.copy()
    for i in range(len(ingredients)):
        if allergen in allergens[i]:
            common_ingredients &= ingredients[i]
    other_ingredients = all_ingredients - common_ingredients
    for other_ingredient in other_ingredients:
        ingredient_allergens[other_ingredient] -= {allergen}

ingredient_candidates = {k: v for k, v in ingredient_allergens.items() if len(v) > 0}
print(ingredient_candidates)

ingredient_allergen_mapping = []
while len(ingredient_candidates) > 0:
    for ing, allers in ingredient_candidates.items():
        if len(allers) == 1:
            aller = allers.pop()
            ingredient_allergen_mapping.append((ing, aller))
            del ingredient_candidates[ing]
            for new_allers in ingredient_candidates.values():
                new_allers -= {aller}
            break

print(ingredient_allergen_mapping)

print(",".join(t[0] for t in sorted(ingredient_allergen_mapping, key=itemgetter(1))))
