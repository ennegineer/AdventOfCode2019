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

def PartOne():
    # Prepare Part One dataset
    one_data = [int(i) for i in data.copy()]
    # Replace postions one and two
    one_data[1] = 12
    one_data[2] = 2

    position = 0

    for i, _ in enumerate(one_data):

        if i < position:
            print(f'Step {position}: less than i ({i}), skip')
            continue

        if one_data[i] == 1:
            calc1 = one_data[i+1]
            calc2 = one_data[i+2]
            calculator = one_data[calc1] + one_data[calc2]
            pos = one_data[i+3]
            print(f'Step {position}: running {one_data[i]}. next two positions are {i+1}, {one_data[i+1]} and {i+2}, {one_data[i+2]}. position {i+3} is {one_data[i+3]} and will be {calculator}. position is now {position+4}')
            one_data[pos] = calculator
            position += 4

        elif one_data[i] == 2:
            calc1 = one_data[i+1]
            calc2 = one_data[i+2]
            calculator = one_data[calc1] * one_data[calc2]
            pos = one_data[i+3]
            print(f'Step {position}: running {one_data[i]}. next two positions are {i+1}, {one_data[i+1]} and {i+2}, {one_data[i+2]}. position {i+3} is {one_data[i+3]} and will be {calculator}. position is now {position+4}')
            one_data[pos] = calculator
            position += 4

        elif one_data[i] == 99:
            print(f'Step {position}: running {one_data[i]}. Terminate program. position is now {position}. position 0 is now {one_data[0]}')
            break

        else:
            print(f'error: one_data[i] is {one_data[i]}')

# 6327510 is correct for part one!

#################################################

def run_program(two_data):
    position = 0

    for i, _ in enumerate(two_data):

        if i < position:
            # print(f'Step {position}: less than i ({i}), skip')
            continue

        if two_data[i] == 1:
            calc1 = two_data[i+1]
            calc2 = two_data[i+2]
            calculator = two_data[calc1] + two_data[calc2]
            pos = two_data[i+3]
            two_data[pos] = calculator
            position += 4

        elif two_data[i] == 2:
            calc1 = two_data[i+1]
            calc2 = two_data[i+2]
            calculator = two_data[calc1] * two_data[calc2]
            pos = two_data[i+3]
            two_data[pos] = calculator
            position += 4

        elif two_data[i] == 99:
            print(f'Step {position}: running {two_data[i]}. Terminate program. position is now {position}. position 0 is now {two_data[0]}')
            break

    return two_data[0]

def PartTwo():
    two_data = [int(i) for i in data.copy()]
    # Replace the values at postions one and two. value at 1 is the noun, value at 2 is the verb.
    two_data[1] = 12
    two_data[2] = 2
    # Now, test replacing the noun and verb with numbers between 0 and 99 until we match the expected output.
    for noun in range(100):
        for verb in range(100):
            two_data[1] = noun
            two_data[2] = verb

            output = run_program(two_data)

            if output == 19690720:
                print(100 * noun + verb)
                print(f'noun: {noun} | verb: {verb}')
                break

            if output != 19690720:
                two_data = [int(i) for i in data.copy()]
                # Replace the values at postions one and two. value at 1 is the noun, value at 2 is the verb.
                two_data[1] = 12
                two_data[2] = 2

PartTwo()

# 4112 is the correct answer for part two, but we get a list index out of range error after the answer prints. Line 72.
# Could add error handling, but should also figure out why this line runs after the program should break.