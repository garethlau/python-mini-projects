import random


def compare(guess, number):

    cows = 0
    bulls = 0

    for i in range(len(number)):
        if guess[i] in number:
            if guess[i] == number[i]:
                cows += 1
            else:
                bulls += 1
    print("Cows: " + str(cows))
    print("Bulls: " + str(bulls))


def user_input(guess):
    str_guess = input("Guess: ")
    for i in range(0, 4):
        guess[i] = str_guess[i]
    return guess


if __name__ == "__main__":
    guess = [0, 0, 0, 0]
    number = [0, 0, 0, 0]
    bulls = 0
    cows = 0
    guesses = 0
    playing = True

    print("Welcome to the Cows and Bulls Game!")
    print("Try to guess the computer generated 4 digit number!")
    print("A Cow means you've guessed the right digit in the right place.)")
    print("A Bull means you've guessed the right digit but in the wrong place.)")
    print("Have fun!")

    # Create random 4 digit number
    for i in range(0, 4):
        number[i] = str(random.randint(0, 9))
    # print(number)

    while playing == True:
        user_guess = user_input(guess)
        # print(user_guess)
        compare(guess, number)
        guesses += 1

        if guess == number:
            print("Number of guesses taken: " + str(guesses))
            break
