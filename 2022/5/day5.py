from collections import deque

input = None
with open("input.txt", "r") as file:
    input = file.readlines()


stacks = [deque() for _ in range(9)]

stacks_input = input[:8]

for row in stacks_input:
    row = row.strip("\n")
    stack = 0
    for i in range(0, len(row), 4):
        if row[i+1].isalpha():
            stacks[stack].appendleft(row[i+1])
        stack += 1

instructions = [
    int(instruction)
    for line in input[10:]
    for instruction in line.strip("\n").split()
    if instruction.isnumeric()
]

part_1_stacks = [stack.copy() for stack in stacks]
part_2_stacks = [stack.copy() for stack in stacks]

def crate_mover_9000(instructions, stacks):
    for i in range(0, len(instructions), 3):
        amount = instructions[i]
        source = instructions[i+1] - 1
        destination = instructions[i+2] - 1
        for _ in range(amount):
            stacks[destination].append(stacks[source].pop())

def crate_mover_9001(instructions, stacks):
    for i in range(0, len(instructions), 3):
        amount = instructions[i]
        source = instructions[i+1] - 1
        destination = instructions[i+2] - 1
        row = deque()
        for _ in range(amount):
            row.appendleft(stacks[source].pop())
        stacks[destination].extend(row)

crate_mover_9000(instructions, part_1_stacks)

part1_answer = ""
for stack in part_1_stacks:
    part1_answer += stack.pop()

print(f"Part 1: {part1_answer}")


crate_mover_9001(instructions, part_2_stacks)

part2_answer = ""
for stack in part_2_stacks:
    part2_answer += stack.pop()

print(f"Part 2: {part2_answer}")
