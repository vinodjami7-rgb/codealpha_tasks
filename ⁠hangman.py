import random

def play_hangman():
    # Predefined list of 5 words
    word_list = ["python", "software", "developer", "scripting", "automation"]
    secret_word = random.choice(word_list)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6

    print("--- Welcome to CodeAlpha Hangman! ---")
    print(f"Guess the word. You can make up to {max_incorrect} incorrect guesses.")

    while incorrect_guesses < max_incorrect:
        # Display current word status
        displayed_word = [letter if letter in guessed_letters else "_" for letter in secret_word]
        print("\nWord: " + " ".join(displayed_word))
        print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")
        
        if "_" not in displayed_word:
            print(f"\n🎉 Congratulations! You guessed the word correctly: '{secret_word}'")
            break

        guess = input("Guess a letter: ").lower().strip()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another one!")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            incorrect_guesses += 1

    else:
        print(f"\nGame Over! You've run out of guesses. The word was: '{secret_word}'")

if __name__ == "__main__":
    play_hangman()
