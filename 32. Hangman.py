import random


def get_word():
    with open('SOWPODS-Dictionary.txt', 'r') as file:
        words = list(file)
    word = random.choice(words).strip()
    return word


def get_list_from_string(string):
    character_list = []
    for i in range(0, len(string)):
        c = string[i].upper()
        character_list.append(c)
    return character_list


def get_guess(guessed_characters):
    while True:
        entry = (input("Guess a letter: ")).upper()
        if entry in guessed_characters:
            print("You already guessed that!")
            continue
        elif len(entry) > 1 or len(entry) < 1:
            print("Please enter one letter at a time!")
        else:
            return entry


def check_guess(guess, characters, guessed_list):
    global display
    guessed_list.append(guess)
    for i in range(0, len(characters)):
        if characters[i] == guess:
            display[i] = guess


def beautiful_print(list):
    for i in range(0, len(list)):
        formatted = ' '.join(list)
    print(formatted)


if __name__ == '__main__':
    display = []
    guessed = []
    correct = []
    guess_number = 1


    word = get_list_from_string(get_word())
    print(word)
    print("__________HANGMAN__________ \n"
          "Try to guess the word I'm \n"
          "thinking of! Enter one letter \n"
          "at a time please! This game \n"
          "isn't case sensitive.")

    for i in range(0, len(word)):
        display.append('_')
    display_f = ' '.join(display)
    print(display_f)

    while display != word:
        print("Guess " + str(guess_number))
        guess = get_guess(guessed)
        check_guess(guess, word, guessed)
        beautiful_print(display)
        guess_number += 1