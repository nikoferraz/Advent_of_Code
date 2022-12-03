from string import ascii_lowercase as lowercase, ascii_uppercase as uppercase

LETTER_PRIORITIES = {
    letter: index + 1
    for index, letter in enumerate(lowercase + uppercase)
}

def get_letter_priority(rucksack):
    compartment1 = set(rucksack[:len(rucksack) // 2])
    compartment2 = set(rucksack[len(rucksack) // 2:])
    return sum(
        LETTER_PRIORITIES[letter]
        for letter in compartment1 & compartment2
    )

def get_badge_priority(elf_group):
    rucksack_1, rucksack_2, rucksack_3 = (set(rucksack) for rucksack in elf_group)
    return sum(
        LETTER_PRIORITIES[letter]
        for letter in rucksack_1 & rucksack_2 & rucksack_3
    )

input = None
with open('input.txt', 'r') as file:
    input = file.readlines()

input = [line.strip() for line in input]

priority_sum = 0

for line in input:
    priority_sum += get_letter_priority(line)

badge_priority_sum = 0

for line in range(0, len(input), 3):
    badge_priority_sum += get_badge_priority(input[line:line + 3])

# Part 1 answer
print(f"Part 1: {priority_sum}")

# Part 2 answer
print(f"Part 2: {badge_priority_sum}")