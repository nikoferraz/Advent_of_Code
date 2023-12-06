
def is_possible(game):
    rounds = game.split(":")[1].split(";")
    for round in rounds:
        round = round.strip().split(",")
        for cubes in round:
            quantity, color = cubes.strip().split(" ")
            print(f"{quantity} {color}")
            if color == "blue" and int(quantity) > 14:
                print("too many blue cubes")
                return False
            elif color == "red" and int(quantity) > 12:
                print("too many red cubes")
                return False
            elif color == "green" and int(quantity) > 13:
                print("too many green cubes")
                return False
    return True

def main():
    result = 0
    with open("input.txt", "r") as file:
        for id, line in enumerate(file):
            print(f"Game {id + 1}")
            if is_possible(line):
                print(f"Game {id + 1} is POSSIBLE!")
                result += id + 1
              
    print(result)
    
if __name__ == "__main__":
    main()
