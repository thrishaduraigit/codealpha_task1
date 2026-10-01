import random

# List of 5 predefined words
words = ["python", "apple", "tiger", "house", "chair"]

# Select a random word
word = random.choice(words)

# Create blanks for the word
guessed_word = ["_"] * len(word)

# Store letters already guessed
guessed_letters = []

# Maximum incorrect guesses
incorrect_guesses = 6

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.")

while incorrect_guesses > 0 and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Incorrect guesses left:", incorrect_guesses)

    guess = input("Enter a letter: ").lower()

    # Check whether the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check whether the letter is present in the word
    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    else:
        print("Wrong guess!")
        incorrect_guesses -= 1

# Final result
if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame over!")
    print("The word was:", word)