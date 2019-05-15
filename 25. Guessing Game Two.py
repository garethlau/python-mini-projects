def computer_guess(high_low, prev_guess, max_min):

    if high_low == 'HIGH':
        max_min[1] = prev_guess
        guess = int(prev_guess - ((max_min[1] - max_min[0]) / 2))
    elif high_low == 'LOW':
        max_min[0] = prev_guess
        guess = int(prev_guess + ((max_min[1] - max_min[0]) / 2))
    return guess

def get_high_low():
    while True:
        entry = (input("Was my guess high or low? ")).upper()
        if entry != "HIGH" and entry != "LOW":
            print("Sorry I didn't catch that. Please tell me whether my guess was high or low.")
            continue
        else:
            return entry

def get_number():
    while True:
        try:
            entry = int(input("Enter a number between 0 and 100: "))
        except ValueError:
            print("That is not a valid entry.")
            continue
        if entry < 0 or entry > 100:
            print("Please enter a number between 0 and 100: ")
            continue
        else:
            return entry


if __name__=='__main__':
    guess_count = 1
    max_min = [0, 100]
    number = get_number()
    guess = computer_guess("LOW", 0, max_min)
    print(guess)
    while number != guess:
        high_low = get_high_low()
        guess = computer_guess(high_low, guess, max_min)
        print(guess)
        guess_count += 1
    print("That took " + str(guess_count) + " guesses.")