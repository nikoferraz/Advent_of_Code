'''Advent of Code 2022 - Day 7: No Space Left On Device'''

from collections import defaultdict

input = []
directory_size = defaultdict(int)
path = []

with open("input.txt", "r") as file:
    for line in file.readlines():
        input.append(
            line.strip("\n")
                .split()
        )

for tokens in input:
    if tokens[1] == 'cd':
        if tokens[2] == '..':
            path.pop()
        else:
            path.append(tokens[2])
    elif tokens[0].isnumeric():
        size = int(tokens[0])
        for i in range(1, len(path)+1):
            full_path = '/'.join(path[:i])
            directory_size[full_path] += size

directory_sizes = sorted(directory_size.values()) 

part1_answer = sum(
        size 
        for size 
        in directory_sizes
        if size <= 100_000
)

print(f"Part 1: {part1_answer}")

### Part 2 ###

SYSTEM_DISK_SIZE = 70_000_000
UPDATE_SIZE = 30_000_000
AVAILABLE_DISK_SPACE = SYSTEM_DISK_SIZE - directory_size["/"]
SPACE_NEEDED = UPDATE_SIZE - AVAILABLE_DISK_SPACE

for size in directory_sizes:
    if size >= SPACE_NEEDED:
        print(f"Part 2: {size}")
        break