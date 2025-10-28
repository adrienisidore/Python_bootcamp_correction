import  random

def main():
    print("This is an interactive guessing game!")
    print(" You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game")
    print("Good luck!")
    found = False
    count = 0
    number = random.randint(1, 99)
    while not found:
        guess = input("what is your guess between 1 and 99?\n>>> ")
        while (not guess.isnumeric()):
            if guess == "exit":
                print("Bye")
                return 0
            print("this is not a correct answer.")
            guess = input("what is your guess between 1 and 99?\n>>> ")
        guess = int(guess)
        if guess == number:
            print("Congratulations, you've got it!")
            print(f"You won in {count} attempts!")
            return (0)
        elif guess > number:
            print("Too high!")
        else:
            print("Too low!")
        count += 1
    return (1)

if __name__ == "__main__":
    main()

