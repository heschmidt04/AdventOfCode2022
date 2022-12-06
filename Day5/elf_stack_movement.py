import pprint
pp = pprint.pprint
import re

stack_file = "day5_stack.txt"
movement_file = "movements.txt"

# Part 1
with open(stack_file) as f:
    stack_lines = f.readlines()

stack_lines.reverse()

stack_dict = {}
cm_9001 = {}
for idx in range(9):
    stack_dict[idx + 1] = []
    cm_9001[idx + 1] = []
for stack_line in stack_lines:
    stack_line = stack_line.rstrip('\n')
    for stack_idx in range(9):
        crate = stack_line[stack_idx]
        if crate == " ":
            continue
        stack_dict[stack_idx + 1].append(crate)
        cm_9001[stack_idx + 1].append(crate)
print(f" ----- This is the stack along the Y axis ")
pp(stack_dict)
print(f" ----- This is the stack along the Y axis ")
print(f" -----------------------------------------")

with open(movement_file) as f:
    movement_lines = f.readlines()

for movement_line in movement_lines:
    movement_line = movement_line.strip()
    movement_instructions = re.findall(r'\d+',movement_line)
    move, origin, destination = movement_instructions
    for _ in range(int(move)):
        crate = stack_dict[int(origin)].pop()
        stack_dict[int(destination)].append(crate)

print(f" ----- This is the MOVED stack along the Y axis ")
pp(stack_dict)
print(f" ----- This is the MOVED stack along the Y axis ")

for arr in range(9):
    print(stack_dict[arr + 1][-1])

# Part 2

pp(cm_9001)
print("---------")
for movement_line in movement_lines:
    holding_pen = []
    movement_line = movement_line.strip()
    movement_instructions = re.findall(r'\d+',movement_line)
    move, origin, destination = movement_instructions
    for _ in range(int(move)):
        crate = cm_9001[int(origin)].pop()
        holding_pen.append(crate)
    holding_pen.reverse()
    for crate in holding_pen:
        cm_9001[int(destination)].append(crate)

pp(cm_9001)
print("*************")
for arr in range(9):
    print(cm_9001[arr + 1][-1])
