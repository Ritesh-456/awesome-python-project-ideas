import random

def choose_word():
    words = ["python", "hangman", "computer", "programming", "algorithm", "variable", "function", "loop", "condition", "string"]
    return random.choice(words).upper()

def display_hangman(tries):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |
           |
           |
           -
        """,
        """
           --------
           |      |
           |
           |
           |
           |
           -
        """
    ]
    return stages[tries]

def play_hangman():
    word = choose_word()
    word_letters = set(word)
    guessed_letters = set()
    tries = 6

    print("Welcome to Hangman!")
    print(display_hangman(tries))
    print("_ " * len(word))

    while tries > 0 and word_letters:
        while True:
            guess = input("Guess a letter: ").strip().upper()
            if len(guess) == 1 and guess.isalpha():
                break
            print("Invalid input. Please enter a single alphabetic character.")

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word_letters:
            word_letters.remove(guess)
            guessed_letters.add(guess)
            print("Good guess!")
        else:
            tries -= 1
            guessed_letters.add(guess)
            print("Wrong guess!")

        print(display_hangman(tries))
        word_display = [letter if letter in guessed_letters else "_" for letter in word]
        print(" ".join(word_display))

    if not word_letters:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Sorry, you ran out of tries. The word was: {word}")

if __name__ == "__main__":
    play_hangman()