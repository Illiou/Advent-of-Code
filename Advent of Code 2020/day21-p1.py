import re
import itertools
from io import StringIO

ingredients = []
allergens = []

with open("input/d21.txt") as f:
# with StringIO("""mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
# trh fvjkl sbzzf mxmxvkd (contains dairy)
# sqjhc fvjkl (contains soy)
# sqjhc mxmxvkd sbzzf (contains fish)""") as f:
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

print(ingredient_allergens)
print(sum(sum(1 for product in ingredients if ing in product) for ing, allers in ingredient_allergens.items() if len(allers) == 0))
