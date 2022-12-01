import pprint
pp = pprint.pprint

file = "input.txt"

with open(file) as f:
    lines = f.readlines()

# elves = [[] , [], []]
calories = []
current_elf = []
for line in lines:
    stripped_line = line.strip()
    if stripped_line:
        current_elf.append(int(stripped_line))
    else:
        calories.append(current_elf)
        current_elf = []
# The last elf won't have a new line after so append it
calories.append(current_elf)

# Loop through data to get max calories for Step 1
# max_calories = max_calories

# Sum up the top three calories for the Elves ;-D
summed_calories = []
for elf_calories in calories:
    calories_per_elf = sum(elf_calories)
    summed_calories.append(calories_per_elf)

top_three = sorted(summed_calories)[-3:] # instead of reverse

print(sum(top_three))



