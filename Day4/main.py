# We are trying to recover a lost password! 
# How many different passwords within our given input meet the criteria?
input = '264360-746325'

# Criteria:
    # It is a six-digit number.
    # The value is within the range given in your puzzle input.
    # Two adjacent digits are the same (like 22 in 122345).
    # Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
    # Other than the range rule, the following are true:

    # 111111 meets these criteria (double 11, never decreases).
    # 223450 does not meet these criteria (decreasing pair of digits 50).
    # 123789 does not meet these criteria (no double).

possible_passwords = []
possibilities = 746326 - 264360

import itertools

def PartOne():
    
    for password in range(264360, 746326): #end with 746326
        # skip any with no repeating numbers
        repeat = [len(list(group)) for key, group in itertools.groupby(str(password))]
        if max(repeat) > 1:
            # next, inspect each password digit by digit...
            digits = [int(i) for i in str(password)]
            increase = [1 if digits[i] < digits[i+1] else -1 if digits[i] > digits[i+1] else 0 for i in range(len(digits)-1)]

            if min(increase) >= 0:
                possible_password = ''.join([str(x) for x in digits])
                possible_passwords.append(possible_password)
 
PartOne()
print(len(set(possible_passwords)))
print(possibilities)
# 945 is correct!