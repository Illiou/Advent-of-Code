problem_file_path = "input/d1.txt"

with open(problem_file_path, "r") as problem_file:
	values = [int(i) for i in problem_file]


count = -1
last_window = -1

for i in range(len(values) - 2):
	window = sum(values[i:i + 3])
	if window > last_window:
		count += 1
	last_window = window

print(count)
