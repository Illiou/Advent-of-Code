problem_file_path = "input/d7.txt"

with open(problem_file_path, "r") as problem_file:
    pos = [int(e) for e in problem_file.readline().split(",")]

pos.sort()

mean = sum(pos) // len(pos)

fuel = sum(((n := abs(p - mean)) + 1) * n // 2 for p in pos)

print(mean, fuel)
