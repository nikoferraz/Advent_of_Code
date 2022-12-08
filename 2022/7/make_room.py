from collections import defaultdict

input = []
with open("input.txt", "r") as file:
    for line in file.readlines():
        input.append(line.strip("\n").split())

print(input)