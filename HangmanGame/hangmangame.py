import random
HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\  |
    / \  |
        ===
    """
]

CATEGORIES = {
    "1": ("Programming", ["python", "developer", "keyboard", "software", "database"]),
    "2": ("Animals", ["elephant", "dolphin", "giraffe", "kangaroo", "penguin"]),
    "3": ("Countries", ["india", "canada", "germany", "australia", "japan"])
}

def choose_category():
    print("\n--- SELECT A CATEGORY ---")
    for key, (category_name, _) in CATEGORIES.items():
        print(f"{key}. {category_name}")
    
    while True:
        choice = input("Choose a category number (1-3): ").strip()
        if choice in CATEGORIES:
            return CATEGORIES[choice]
        print("❌ Invalid selection. Please enter 1, 2, or 3.")

def play_hangman():
    wins = 0
    losses = 0

    while True:
        category_name, words_list = choose_category()
        secret_word = random.choice(words_list)
        
        guessed_letters = []
        wrong_guesses = []
        attempts_remaining = 6
        hint_used = False

        print("\n==================================")
        print(" 🎮 WELCOME TO THE HANGMAN GAME 🎮")
        print("==================================")
        print(f"Category Selected: {category_name.upper()}")
        print("You have 6 incorrect attempts.")
        
        while attempts_remaining > 0: 
            print(HANGMAN_PICS[6 - attempts_remaining])

            displayed_word = [
                letter if letter in guessed_letters else "_"
                for letter in secret_word
            ]

            print("\nWord:", " ".join(displayed_word))
            print("Attempts Left:", attempts_remaining)
            print("Correct Letters:",
                  ", ".join(sorted(guessed_letters)) if guessed_letters else "None")
            print("Wrong Letters:",
                  ", ".join(wrong_guesses) if wrong_guesses else "None")

            if "_" not in displayed_word:
                print("\n🎉 CONGRATULATIONS! YOU WON! 🎉")
                print("You guessed the word:", secret_word.upper())
                wins += 1
                break

            print("\n💡 Type 'hint' to reveal one letter (Only Once)")
            guess = input("Enter a letter: ").lower().strip()

            if guess == "hint":
                if not hint_used:
                    for ch in secret_word:
                        if ch not in guessed_letters:
                            guessed_letters.append(ch)
                            hint_used = True
                            print(f"\n💡 Hint: Letter '{ch.upper()}' has been revealed.")
                            break
                else:
                    print("\n⚠️ Hint already used.")
                continue

            if len(guess) != 1 or not guess.isalpha():
                print("\n❌ Enter only one alphabetical letter.")
                continue

            if guess in guessed_letters or guess in wrong_guesses:
                print("\n⚠️ Letter already guessed.")
                continue

            if guess in secret_word:
                guessed_letters.append(guess)
                print("\n✅ Correct Guess!")
            else:
                wrong_guesses.append(guess)
                attempts_remaining -= 1
                print("\n❌ Wrong Guess!")

        if attempts_remaining == 0:
            print(HANGMAN_PICS[6])
            print("\n💀 GAME OVER")
            print("The correct word was:", secret_word.upper())
            losses += 1

        print("\n------------------------------")
        print(f"📊 CURRENT SCORE: Wins: {wins} | Losses: {losses}")
        print("------------------------------")

        choice = input("\nDo you want to play again? (y/n): ").lower().strip()
        if choice != "y":
            print("\n🙏 Thanks for playing Hangman!")
            print(f"Final Score: {wins} Wins | {losses} Losses")
            print("Have a great day! 👋")
            break

if __name__ == "__main__":
    play_hangman()
