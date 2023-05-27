


import random

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    secret_number = random.randint(1, 100)

    while True:
        guess = int(input("Take a guess: "))

        if guess < secret_number:
            print("Too low. Guess higher!")
        elif guess > secret_number:
            print("Too high, Guess lower!")
        else:
            print("Congratulations! You guessed the correct number.")
            break

def main():
    game()

    if __name__ == "__main__":
        main()
