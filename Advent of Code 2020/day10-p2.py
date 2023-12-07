import re
import itertools

with open("input/d10.txt") as f:
    adapters = [int(i.strip()) for i in f]

adapters.sort()
print(adapters)
adapters_diff = adapters.copy()

adapters.append(max(adapters) + 3)
adapters_diff.insert(0, 0)

diffs = [adapters[i] - adapters_diff[i] for i in range(len(adapters))]
print(diffs)


arrangements = 1
diff_iter = iter(range(len(diffs) - 1))

for i in diff_iter:
    # index free?
    if diffs[i] == 1 and diffs[i + 1] == 1:
        streak_count = 1
        next(diff_iter)
        # find remaining free indices on streak
        try:
            while diffs[next(diff_iter)] == 1:
                streak_count += 1
        except StopIteration:
            pass

        count = 0
        for prod in itertools.product("01", repeat=streak_count):
            s = "".join(prod)
            if not re.search(r"000+", s):
                count += 1
        arrangements *= count

print(arrangements)
