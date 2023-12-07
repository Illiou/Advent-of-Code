problem_file_path = "input/d1.txt"

count = -1

with open(problem_file_path, "r") as problem_file:
	last_line = -1
	for line in problem_file:
		if int(line) > last_line:
			count += 1
		last_line = int(line)

print(count)
