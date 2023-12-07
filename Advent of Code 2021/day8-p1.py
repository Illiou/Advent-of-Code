problem_file_path = "input/d8.txt"

with open(problem_file_path, "r") as problem_file:
    patterns = []
    output = []
    for line in problem_file:
        i, o = line.split(" | ")
        patterns.append(i.split())
        output.append(o.split())

counts = sum(1 for display in output for o in display if len(o) in [2, 3, 4, 7])

print(counts)
