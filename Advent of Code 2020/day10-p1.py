
with open("input/d10.txt") as f:
    adapters = [int(i.strip()) for i in f]

adapters.sort()
adapters_diff = adapters.copy()

adapters.append(max(adapters) + 3)
adapters_diff.insert(0, 0)

diffs = [adapters[i] - adapters_diff[i] for i in range(len(adapters))]

print(diffs.count(1) * diffs.count(3))
