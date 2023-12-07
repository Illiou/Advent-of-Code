problem_file_path = "input/d3.txt"

with open(problem_file_path, "r") as problem_file:
    numbers = [list(l.strip()) for l in problem_file]

gamma = ""
epsilon = ""
for i in range(len(numbers[0])):
    if [l[i] for l in numbers].count("1") > len(numbers) / 2:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print(gamma, epsilon, int(gamma, 2) * int(epsilon, 2))
