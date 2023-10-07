import math

# Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module, take its mass, divide by three, round down  (floor?), and subtract 2.

# Import the data
with open("input.txt", "r") as input:
    data = input.read().split('\n')

counter = 0

for row in data:
    calc = math.floor(int(row) / 3) - 2
    counter += calc

print(counter)

