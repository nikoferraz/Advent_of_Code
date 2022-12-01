'''variable input reads a text file'''
input = None
# Save file as list in input variable
with open('input.txt', 'r') as file:
    input = file.readlines()

calories = []
elf = []
for line in input:
    if line == "\n":
        calories.append(sum(elf))
        elf.clear()
    else:
        elf.append(int(line.strip()))

calories.sort()
# Day 1, part 1
print(calories[-1:])

# Day 1, part 2
print(sum(calories[-3:]))
