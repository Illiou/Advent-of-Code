problem_file_path = "input/d7.txt"

with open(problem_file_path, "r") as problem_file:
    pos = [int(e) for e in problem_file.readline().split(",")]

pos.sort()

median = pos[len(pos) // 2]

fuel = sum(abs(p - median) for p in pos)

print(median, fuel)
