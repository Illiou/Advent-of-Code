problem_file_path = "input/d8.txt"

with open(problem_file_path, "r") as problem_file:
    patterns = []
    output = []
    for line in problem_file:
        i, o = line.split(" | ")
        patterns.append(i.split())
        output.append(o.split())

segment_names = "abcdefg"
segment_names_set = set(segment_names)
seven_segment = {"abcefg" : "0",
                 "cf" : "1",
                 "acdeg" : "2",
                 "acdfg" : "3",
                 "bcdf" : "4",
                 "abdfg" : "5",
                 "abdefg" : "6",
                 "acf" : "7",
                 "abcdefg" : "8",
                 "abcdfg" : "9"}
seven_segment_counts = {letter: sum(number.count(letter) for number in seven_segment.keys()) for letter in segment_names}

output_sum = 0

for i in range(len(patterns)):
    numbers = sorted(patterns[i], key=len)
    cable_mapping_possibilities = {l:set(segment_names) for l in segment_names}
    for num in numbers:
        possible_letters = set()
        for k in seven_segment.keys():
            if len(num) == len(k):
                possible_letters.update(k)
        excluded_set = segment_names_set.difference(possible_letters)
        for letter in segment_names:
            if letter in num:
                cable_mapping_possibilities[letter] -= excluded_set
            elif len(possible_letters) < len(segment_names):
                cable_mapping_possibilities[letter] -= possible_letters

    for letter in segment_names:
        count_ = sum(number.count(letter) for number in numbers)
        for l, c in seven_segment_counts.items():
            if count_ != c:
                cable_mapping_possibilities[letter].difference_update([l])

    translation_map = str.maketrans({cable: s.pop() for cable, s in cable_mapping_possibilities.items()})
    output_value = ""
    for out in output[i]:
        output_value += seven_segment["".join(sorted(out.translate(translation_map)))]
    output_sum += int(output_value)

print(output_sum)
