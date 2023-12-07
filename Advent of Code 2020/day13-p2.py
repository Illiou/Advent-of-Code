
with open("input/d13.txt") as f:
    f.readline()
    busses = [(int(bus), offset) for offset, bus in enumerate(f.readline().split(",")) if bus != "x"]

print(busses)

cycle_plus_offset = -1
cycle_length = 1
for bus, offset in busses:
    if cycle_plus_offset == -1:
        cycle_plus_offset = bus
        cycle_length = bus
        continue
    last_cycle_plus_offset = cycle_plus_offset
    for i in range(bus):
        cycle_plus_offset = last_cycle_plus_offset + (cycle_length * i)
        if (cycle_plus_offset + offset) % bus == 0:
            break
    cycle_length *= bus

print(cycle_plus_offset)
