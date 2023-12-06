import re


def main():
    input = []
    with open("input.txt", "r") as file:
        for line in file:
            input.append("".join(re.findall(r"\d+", line)))
    total = 0
    for digit in input:
        total += int(digit[0] + digit[-1])
    print(total)


if __name__ == "__main__":
    main()
