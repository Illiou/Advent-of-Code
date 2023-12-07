problem_file_path = "input/d6.txt"

with open(problem_file_path, "r") as problem_file:
    fish = [int(e) for e in problem_file.readline().split(",")]

for day in range(80):
    for i in range(len(fish)):
        if fish[i] == 0:
            fish[i] = 6
            fish.append(8)
        else:
            fish[i] -= 1

print(len(fish))