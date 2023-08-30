
import random

def choose_word():
    word_list = ["cat", "human", "hang", "game", "hero", "note", "apple"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def game():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Guess the letters to reveal the hidden word.")
    
    while attempts > 0:
        display = display_word(word, guessed_letters)
        print(display)
        
        if display == word:
            print("Congratulations! You guessed the word!")
            break
        
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            print("Correct guess!")
        else:
            guessed_letters.append(guess)
            attempts -= 1
            print("Incorrect guess. Attempts left:", attempts)
        
        if attempts == 0:
            print("Sorry, you're out of attempts. The word was:", word)
            break

game()
