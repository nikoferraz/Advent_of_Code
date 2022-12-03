LETTER_PLAY = {
    "A": "Rock",
    "X": "Rock",
    "B": "Paper",
    "Y": "Paper",
    "C": "Scissors",
    "Z": "Scissors",
}
STRATEGY = {
    "X": "Lose",
    "Y": "Draw",
    "Z": "Win",
}
PLAY_SCORE = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3,
}
GAME_POINT = {
    "Draw": 3,
    "Win": 6,
    "Lose": 0,
}

def rock_paper_scissors(elf, you):
    elf = LETTER_PLAY[elf]
    you = LETTER_PLAY[you]
    score = PLAY_SCORE[you]
    if elf == you:
        score += GAME_POINT["Draw"]
    elif elf == "Rock" and you == "Paper":
        score += GAME_POINT["Win"]
    elif elf == "Paper" and you == "Scissors":
        score += GAME_POINT["Win"]
    elif elf == "Scissors" and you == "Rock":
        score += GAME_POINT["Win"]
    else:
        score += GAME_POINT["Lose"]
    return score

def rock_paper_scissors_part_2(elf, strategy):
    if strategy == "Lose":
        if elf == "A":
            return rock_paper_scissors(elf, "C")
        if elf == "B":
            return rock_paper_scissors(elf, "A")
        if elf == "C":
            return rock_paper_scissors(elf, "B")
    if strategy == "Draw":
        return rock_paper_scissors(elf, elf)

    if elf == "A":
        return rock_paper_scissors(elf, "B")
    if elf == "B":
        return rock_paper_scissors(elf, "C")
    if elf == "C":
        return rock_paper_scissors(elf, "A")

input = None
with open('input.txt', 'r') as file:
    input = file.readlines()

total_score = 0
for line in input:
    elf, you = line.strip().split()
    total_score += rock_paper_scissors(elf, you)

# Day 1, part 1
print(f"Part 1 answer: {total_score}")


total_score = 0
for line in input:
    elf, strategy = line.strip().split()
    total_score += rock_paper_scissors_part_2(elf, STRATEGY[strategy])  # type: ignore

# Day 1, part 2
print(f"Part 2 answer: {total_score}")
    