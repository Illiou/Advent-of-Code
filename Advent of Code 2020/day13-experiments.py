
# first = 7
# second = 13
# third = 5
#
# for i in range(1000):
#     first_print = "D" if i % first == 0 else "."
#     second_print = "D" if i % second == 0 else "."
#     third_print = "D" if i % third == 0 else "."
#     print(f"{i}: {first_print} {second_print} {third_print}")

first = 23
second = 41

for i in range(1000):
    first_print = "D" if i % first == 0 else "."
    second_print = "D" if i % second == 0 else "."
    print(f"{i}: {first_print} {second_print}")


offset = 17

big = max(first, second)
small = min(first, second)

difference = big - small
rollover_amount = small - (big % small)

offset_to_last = offset % small

# difference - rollover_amount * rollover_times = offset
offset_difference = difference - offset_to_last
if offset_difference < 0:
    offset_difference =  first - offset_difference
rollover_times = offset_difference // rollover_amount

difference_rollover_amount = rollover_amount - (small % rollover_amount)
difference_rollover_times = (offset_difference % rollover_amount) // difference_rollover_amount

difference_rollover_factor = small // rollover_amount + 1

# rollover time is one less than total times needed
big_result = big * (rollover_times + 1) + big * difference_rollover_factor * difference_rollover_times

small_result = big_result - offset

print(small_result, big_result)
