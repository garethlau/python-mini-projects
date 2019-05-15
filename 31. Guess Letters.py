def get_list_from_string(string):
    character_list = []
    for i in range(0, len(string)):
        c = string[i].upper()
        character_list.append(c)
    return character_list


def get_guess(guessed_characters):
    guess = []
    status = True
    while status:
        entry = input("Guess a letter: ")
        for i in range(0, len(entry)):
            character = entry[i].upper()
            guess.append(character)
        if character in guessed_characters:
            print("You already guessed " + character)
        elif character not in guessed_characters and i == len(entry):
            status = False


def check_guess(guess, characters, guessed_list):
    global display
    for i in range(0, len(guess)):
        guessed_list.append(guess[i])
        for n in range(0, len(characters)):
            if characters[n] == guess:
                display[n] = guess


def beautiful_print(list):
    for i in range(0, len(list)):
        formatted = ' '.join(list)
    print(formatted)


if __name__ == '__main__':
    display = []
    guessed = []
    correct = []
    guess_number = 1

    word = get_list_from_string('AniMal')

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
        print(guess)
        check_guess(guess, word, guessed)
        beautiful_print(display)
        guess_number += 1