problem_file_path = "input/d6.txt"

with open(problem_file_path, "r") as problem_file:
    fish = [int(e) for e in problem_file.readline().split(",")]

# ages = [0 for _ in range(9)]
# for f in fish:
#     ages[f] += 1

ages = [fish.count(age) for age in range(9)]

for day in range(256):
    ages[7] += ages[0]
    ages.append(ages.pop(0))

print(sum(ages))