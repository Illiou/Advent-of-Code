from operator import itemgetter

with open("input/d13.txt") as f:
    time = int(f.readline())
    busses = [int(id) for id in f.readline().split(",") if id != "x"]

bus, wait_time = min(((bus, bus - (time % bus)) for bus in busses), key=itemgetter(1))

print(bus, wait_time)
print(bus * wait_time)