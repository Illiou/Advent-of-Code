
with open("input/d25.txt") as f:
    pk1 = int(f.readline())
    pk2 = int(f.readline())

subject_number = 7
value = 1
loop_size = 0
while value != pk1:
    value *= subject_number
    value %= 20201227
    loop_size += 1

print(value)

encryption_key = 1
for i in range(loop_size):
    encryption_key *= pk2
    encryption_key %= 20201227
    loop_size += 1

print(encryption_key)
