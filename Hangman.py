import random

words = ("apple", "microsoft", "leetcode", "mongodb", "mango")

Hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    1: (" o ",
        "   ",
        "   "),
    2: (" o ",
        " | ",
        "   "),
    3: (" o ",
        "/| ",
        "   "),
    4: (" o ",
        "/|\\",
        "   "),
    5: (" o ",
        "/|\\",
        "/  "),
    6: (" o ",
        "/|\\",
        "/ \\")
}

def display_man(wrong_guess):
    print("************")
    for line in Hangman_art[wrong_guess]:
        print(line)
    print("************")

def display_hint(hint):
    print(" ".join(hint))

def main():
    ans = random.choice(words)  # Select a random word
    hint = ["_"] * len(ans)  # Create blanks for the word
    wrong_guess = 0
    guessed_letters = set()

    while wrong_guess < 6 and "_" in hint:
        display_man(wrong_guess)
        display_hint(hint)

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try another letter.")
            continue

        guessed_letters.add(guess)

        if guess in ans:
            for i in range(len(ans)):
                if ans[i] == guess:
                    hint[i] = guess  
        else:
            wrong_guess += 1
        
        display_man(wrong_guess)
    if "_" not in hint:
        print("🎉 Congratulations! You guessed the word:", ans)
    else:
        print("Game Over! The correct word was:", ans)

if __name__ == "__main__":
    main()