import random

def game():
    print("Welcome to the Random Number Guessing Game!")
    limit = int(input("Enter the upper limit for the random number: "))
    secret_number = random.randint(1, limit)
    tries = 0

    while True:
        guess = int(input("Enter your guess: "))
        tries += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} in {tries} tries.")
            break

game()
