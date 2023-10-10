# intcode
# 1: adds together next two index's numbers, overwrites 3rd position
# 2: multiplies ... then step forward 4 positions

# If value of i = 1, take i+1 then value at index i+1, add i+2 value, overwrite i+3, update i to i+4
# If value if i = 99, halt program
# Before running the program, replace position 1 with value 12, and position 2 with value 2.
# What value is left at position 0 after program halts?

# Import the data
with open("input.txt", "r") as input:
    data = input.read().split(',')
# print(data)

def PartOne():
    # Prepare Part One dataset
    one_data = [int(i) for i in data.copy()]
    # Replace postions one and two
    one_data[1] = 12
    one_data[2] = 2

    # print(data[2])
    # print(one_data)

    position = 0

    for i, _ in enumerate(one_data):

        if i < position:
            print(f'Step {position}: less than i ({i}), skip')
            continue

        if one_data[i] == 1:

            calculator = one_data[i+1] + one_data[i+2]
            pos = one_data[i+3]
            # print(f'calculator: {calculator}')
            # print(one_data[3])
            print(f'Step {position}: running {one_data[i]}. next two positions are {i+1}, {one_data[i+1]} and {i+2}, {one_data[i+2]}. position {i+3} is {one_data[i+3]} and will be {calculator}. position is now {position+4}')
            one_data[pos] = calculator
            position += 4
            # print(f'position is now {i}')

        elif one_data[i] == 2:

            calculator = one_data[i+1] * one_data[i+2]
            pos = one_data[i+3]
            # print(f'calculator: {calculator}')
            # print(one_data[3])
            print(f'Step {position}: running {one_data[i]}. next two positions are {i+1}, {one_data[i+1]} and {i+2}, {one_data[i+2]}. position {i+3} is {one_data[i+3]} and will be {calculator}. position is now {position+4}')
            one_data[pos] = calculator
            position += 4

        elif one_data[i] == 99:
            print(f'Step {position}: running {one_data[i]}. Terminate program. position is now {position}. position 0 is now {one_data[0]}')
            # print(one_data)
            break

        else:
            print(f'error: one_data[i] is {one_data[i]}')

PartOne()
# 160 is too low.

