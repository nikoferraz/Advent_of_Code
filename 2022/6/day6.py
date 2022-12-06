input = None
with open("input.txt", "r") as file:
    input = file.readlines()

input = input[0].strip("\n")

for i in range(0, len(input) - 4, 1):
    if len(set(input[i:i+4])) == 4:
        print(f"Part 1 answer {i+4}")
        break

for i in range(0, len(input) - 14, 1):
    if len(set(input[i:i+14])) == 14:
        print(f"Part 2 answer {i+14}")
        break