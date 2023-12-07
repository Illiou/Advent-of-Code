
input_numbers = "0,5,4,1,10,14,7"

input_numbers = [int(e) for e in input_numbers.split(",")]

number_last_said = {}
last_number = input_numbers[0]

for turn in range(2, 2021):
    if turn <= len(input_numbers):
        number_last_said[last_number] = turn - 1
        last_number = input_numbers[turn - 1]
    elif last_number in number_last_said:
        turn_difference = turn - 1 - number_last_said[last_number]
        number_last_said[last_number] = turn - 1
        last_number = turn_difference
    else:
        number_last_said[last_number] = turn - 1
        last_number = 0

print(number_last_said)
print(last_number)
