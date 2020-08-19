import random
import time


def main():
    global count
    global display
    global word_to_guess
    global already_guessed
    global length
    global play_game
    words = ["january", "border", "image", "film", "promise", "kids", "lungs", "doll", "rhyme", "damage",
             "plants"]
    word_to_guess = random.choice(words)
    length = len(word_to_guess)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""


def play_loop():
    global play_game
    play_game = input("Do you want to play again? y = yes, n = no \n")
    while play_game not in {"y", "n", "Y", "N"}:
        play_game = input("Do you want to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks for playing! We expect you back again!")
        exit()


def hangman():
    global count
    global display
    global word_to_guess
    global already_guessed
    global play_game
    limit = 10
    guess = input('This is the Hangman Word: ' + display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()
    elif guess in word_to_guess:
        already_guessed.extend([guess])
        index = word_to_guess.find(guess)
        word_to_guess = word_to_guess[:index] + "_" + word_to_guess[index+1:]
        display = display[:index] + guess + display[index+1:]
        print(display+"\n")
    elif guess in already_guessed:
        print("Try another letter.\n")
    else:
        count += 1
        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + "guess remaining\n")
        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + "guess remaining\n")
        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")
        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:", already_guessed, word_to_guess)
            play_loop()
    if word_to_guess == "_" * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()
    elif count != limit:
        hangman()


print("\nWelcome to Hangman game\nBest of Luck!\n")
time.sleep(2)
print("The game is about to start!\nLet's play Hangman!")
time.sleep(3)
main()
hangman()
