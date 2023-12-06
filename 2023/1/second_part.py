import re

DIGIT = {
    "one": "1",
    "two": "2",
    "three": "3", 
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9",
}
WORDS = DIGIT.keys()

def parse_line(line):
    digits = []
    for ind, ch in enumerate(line):
        if ch.isdigit():
            digits.append(ch)
            continue
        for word in WORDS:
            if line[ind:].startswith(word):
                digits.append(DIGIT[word])
    return "".join(digits)

def main():
    total = 0
    with open("input.txt", "r") as file:
        for line in file:
          newline = parse_line(line)  
          total += int(newline[0] + newline[-1])
    print(total) 

if __name__ == "__main__":
    main()
