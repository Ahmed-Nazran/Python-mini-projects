import random

while True:
    input("Press Enter to roll the dice...")
    roll = random.randint(1, 6)
    print(f"You rolled: {roll}")
    play_again = input("Roll again? (y/n): ")
    if play_again.lower() != "y":
        break
