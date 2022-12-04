import pprint
pp = pprint.pprint

file = "day3_input.txt"

# put a 0 in front to offset python idx start versus count start
lookup = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Part 1
with open(file) as f:
    lines = f.readlines()

sum_priorities = 0

for line in lines:
    line = line.strip()
    line_length = len(line)
    compartment_length = int(line_length / 2)
    compartment_1 = line[:compartment_length]
    compartment_2 = line[compartment_length:]
    # print(compartment_1 + "-spacer-" + compartment_2)
    for char in compartment_1:
        if char in compartment_2:
            priority = lookup.index(char)
            sum_priorities += priority
            break

print(sum_priorities)

# Part 2
elf_group = []
sum_priorities = 0

for line in lines:
    line = line.strip()
    elf_group.append(line)
    if len(elf_group) == 3:
        elves = [{}, {}, {}]
        for idx in range(3):
            for char in elf_group[idx]:
                elves[idx][char] = 0
        for key in elves[0].keys():
            if key in elves[1].keys() and key in elves[2].keys():
                priority = lookup.index(key)
                sum_priorities += priority
                break # after the first common key of all 3 elves, don't need to look more
        elf_group = []


print(sum_priorities)

# Part 3

elf_group = []
sum_priorities = 0

for line in lines:
    line = line.strip()
    elf_group.append(line)
    if len(elf_group) == 3:
        elves = [set(), set(), set()]
        for idx in range(3):
            for char in elf_group[idx]:
                elves[idx].add(char)
        for key in elves[0]:
            if key in elves[1] and key in elves[2]:
                priority = lookup.index(key)
                sum_priorities += priority
                break # after the first common key of all 3 elves, don't need to look more
        elf_group = []


print(sum_priorities)


