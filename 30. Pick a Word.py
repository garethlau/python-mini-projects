import random

if __name__=='__main__':
    words = []
    with open('SOWPODS-Dictionary.txt', 'r') as file:
        words = list(file)
    word = random.choice(words).strip()
    print(word)
