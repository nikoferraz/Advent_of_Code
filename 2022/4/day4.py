input = None
with open("input.txt", "r") as file:
    input = file.readlines()

input = [pair.split("-") for line in input for pair in line.strip().split(",")]

input = tuple((int(pair[0]), int(pair[1])) for pair in input)

total_ranges_contained = 0

for i in range(0, len(input), 2):
    range_start, range_end = input[i][0], input[i][1]
    range2_start, range2_end = input[i + 1][0], input[i + 1][1]
    if range_start <= range2_start and range2_end <= range_end:
        total_ranges_contained += 1
    elif range2_start <= range_start and range_end <= range2_end:
        total_ranges_contained += 1

overlapping_pairs = 0

for i in range(0, len(input), 2):
    range_start, range_end = input[i][0], input[i][1]
    range2_start, range2_end = input[i + 1][0], input[i + 1][1]
    if range_start <= range2_start <= range_end:
        overlapping_pairs += 1
    elif range2_start <= range_start <= range2_end:
        overlapping_pairs += 1


# Part 1 answer
print(f"Part 1: {total_ranges_contained}")

# Part 2 answer
print(f"Part 2: {overlapping_pairs}")
