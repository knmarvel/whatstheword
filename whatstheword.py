import requests
import random

API = "https://random-word-api.herokuapp.com/word?number=10"


def compare(guess, chosen):
    correct_placement = 0
    correct_letter = 0
    for index, letter in enumerate(guess):
        try:
            if chosen[index] == letter:
                correct_placement += 1
        except IndexError:
            continue
        if letter in chosen:
            correct_letter += 1
    if correct_placement or correct_letter:
        print(f"{correct_placement} letters are in the right place")
        print(f"{correct_letter} total letters are correct")
    else:
        print("poop emoji")


def guessing(words, chosen):
    guess = input("Guess a word and I'll tell you how right you are\n")
    if guess == chosen:
        print("You win! Fireworks yay")
        return "Winner"
    elif guess not in words:
        print("Please pick a word from the list, thanks")
        return "Bad guess"
    else:
        compare(guess, chosen)
        return "Bad guess"


def main():
    name = input("What's your name?\n")
    words = requests.get(API)
    printed_words = "\n".join(words.json())
    print(f"Hi, {name}, here's your list of words:\n", printed_words)
    chosen_word = random.choice(words.json())
    print(f"{name}, you get 3 guesses.")
    counter = 3
    while counter > 0:
        result = guessing(words.json(), chosen_word)
        if result == "Winner":
            counter = 0
        else:
            counter -= 1
            print(f"you have {counter} more tries")
    if result != "Winner":
        print("Loser, double loser, as if, whatever, moron")
        print(f"Correct word: {chosen_word}")


if __name__ == "__main__":
    main()
