import math

# Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module, take its mass, divide by three, round down  (floor?), and subtract 2.

# Import the data
with open("input.txt", "r") as input:
    data = input.read().split('\n')

def PartOne():
    counter = 0

    for row in data:
        calc = math.floor(int(row) / 3) - 2
        counter += calc

    print(counter)
    # 3317659 is correct!

# Part two!
# Fuel itself requires fuel just like a module - take its mass, divide by three, round down, and subtract 2. However, that fuel also requires fuel, and that fuel requires fuel, and so on. Any mass that would require negative fuel should instead be treated as if it requires zero fuel; the remaining mass, if any, is instead handled by wishing really hard, which has no mass and is outside the scope of this calculation.

def PartTwo():
    fuel_counter = 0

    for row in data:
        calc = math.floor(int(row) / 3) - 2
        fuel_counter += calc
        while calc > 0:
            calc = math.floor(int(calc) / 3) - 2
            if calc > 0:
                fuel_counter += calc
            if calc <= 0:
                break

    print(fuel_counter)
    # 6635318 was too high!
    # 6629463 was too high!
    # 4973506 was too low!
    # 4973616 was correct!

PartTwo()