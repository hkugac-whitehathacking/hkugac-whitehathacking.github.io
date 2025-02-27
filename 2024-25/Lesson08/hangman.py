import sqlite3
import random

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("hangman_words.db")
cursor = conn.cursor()

# Create table for words if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS words (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word TEXT UNIQUE NOT NULL
)
""")
conn.commit()

# Default word list (only inserted if the table is empty)
default_words = ["python", "developer", "hangman", "database", "programming",
                 "computer", "science", "algorithm", "function", "variable"]

# Insert default words if table is empty
cursor.execute("SELECT COUNT(*) FROM words")
if cursor.fetchone()[0] == 0:
    cursor.executemany("INSERT INTO words (word) VALUES (?)", [(w,) for w in default_words])
    conn.commit()

# Function to get a random word from the database
def get_random_word():
    cursor.execute("SELECT word FROM words ORDER BY RANDOM() LIMIT 1")
    return cursor.fetchone()[0]

# Function to add a word to the database
def add_word():
    new_word = input("Enter a new word to add: ").strip().lower()
    try:
        cursor.execute("INSERT INTO words (word) VALUES (?)", (new_word,))
        conn.commit()
        print(f"✅ '{new_word}' added successfully!")
    except sqlite3.IntegrityError:
        print("⚠️ This word already exists!")

# Function to remove a word from the database
def remove_word():
    word_to_remove = input("Enter the word to remove: ").strip().lower()
    cursor.execute("DELETE FROM words WHERE word = ?", (word_to_remove,))
    if cursor.rowcount > 0:
        conn.commit()
        print(f"❌ '{word_to_remove}' removed successfully!")
    else:
        print("⚠️ Word not found in the list!")

# Function to view all words
def view_words():
    cursor.execute("SELECT word FROM words")
    words = cursor.fetchall()
    print("\n📜 **Word List:**")
    for idx, word in enumerate(words, 1):
        print(f"{idx}. {word[0]}")
    print()

# Hangman game logic
def play_hangman():
    word = get_random_word()
    guessed_letters = set()
    attempts = 6
    word_display = ["_" for _ in word]

    print("\n🎮 **Welcome to Hangman!** 🎮")
    print("Guess the word letter by letter.\n")

    while attempts > 0:
        print("\nWord: ", " ".join(word_display))
        print(f"❌ Wrong guesses left: {attempts}")
        print(f"🔤 Guessed letters: {' '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

        guess = input("Enter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("🔁 You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("✅ Correct!")
            for i, letter in enumerate(word):
                if letter == guess:
                    word_display[i] = guess
        else:
            print("❌ Incorrect!")
            attempts -= 1

        if "_" not in word_display:
            print("\n🎉 **Congratulations! You guessed the word:**", word.upper())
            return

    print("\n💀 **Game Over!** The word was:", word.upper())

# Menu for the game
def menu():
    while True:
        print("\n🎲 **HANGMAN MENU** 🎲")
        print("1️⃣ Play Hangman")
        print("2️⃣ Add a Word")
        print("3️⃣ Remove a Word")
        print("4️⃣ View Word List")
        print("5️⃣ Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            play_hangman()
        elif choice == "2":
            add_word()
        elif choice == "3":
            remove_word()
        elif choice == "4":
            view_words()
        elif choice == "5":
            print("👋 Exiting... Goodbye!")
            conn.close()
            break
        else:
            print("⚠️ Invalid option! Please try again.")

# Run the menu
if __name__ == "__main__":
    menu()