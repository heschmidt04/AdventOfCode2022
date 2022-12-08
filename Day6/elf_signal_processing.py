import pprint
pp = pprint.pprint
import re

signal_file = "day6_input.txt"

# Part 1
with open(signal_file) as f:
    signal_line = f.read()

signal_line = signal_line.strip()

print(len(signal_line))

index = 0
comparison = []
for char in signal_line:
    index += 1
    comparison.append(char)
    if len(comparison) == 5:
        comparison.pop(0)

    if len(comparison) == 4:
        print(comparison)
        # The set removes the duplicates making comparison for 4 unique vals less than 4 if NOT unique
        comparison_set = set(comparison)
        if len(comparison_set) == 4:
            print(index)
            break

# Part 2
index = 0
comparison = []
for char in signal_line:
    index += 1
    comparison.append(char)
    if len(comparison) == 15:
        comparison.pop(0)

    if len(comparison) == 14:
        print(comparison)
        # The set removes the duplicates making comparison for 4 unique vals less than 4 if NOT unique
        comparison_set = set(comparison)
        if len(comparison_set) == 14:
            print(index)
            break


