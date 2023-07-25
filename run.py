import sys
from fizzbuzz import FizzBuzzGame, Fizz, Buzz, FizzBuzz

def main():
    if len(sys.argv) != 3:
        print("Usage: python run.py <number> <game>")
        return

    number = int(sys.argv[1])
    game_name = sys.argv[2]

    rules = []

    if game_name.lower() == "fizz":
        rules.append(Fizz())
    elif game_name.lower() == "buzz":
        rules.append(Buzz())
    elif game_name.lower() == "fizzbuzz":
        rules.append(FizzBuzz())
    else:
        print("Invalid game name. Choose 'Fizz', 'Buzz', or 'FizzBuzz'.")
        return

    game = FizzBuzzGame(rules)
    result = game.play(number)
    print(result)

if __name__ == "__main__":
    main()
