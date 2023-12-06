
def get_power(game):
    rounds = game.split(":")[1].split(";")
    max_red, max_blue, max_green = 0,0,0
    for round in rounds:
        round = round.strip().split(",")
        for cubes in round:
            quantity, color = cubes.strip().split(" ")
            quantity = int(quantity)
            if color == "blue" and quantity > max_blue:
                max_blue = quantity
            elif color == "red" and quantity > max_red:
                max_red = quantity
            elif color == "green" and quantity > max_green:
                max_green = quantity
    return max_red * max_blue * max_green

def main():
    result = 0
    with open("input.txt", "r") as file:
        for line in file:
            result += get_power(line)
              
    print(result)
    
if __name__ == "__main__":
    main()
