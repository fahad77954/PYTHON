import random

while True:
    try:
        level = int(input("Level: "))
        if level <= 0:
            raise ValueError
        else:
            break
    except ValueError:
        pass
value = random.randint(1, level)
while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            raise ValueError
        else:
            if guess < value:
                print("Too small!")
            elif guess > value:
                print("Too large!")
            elif guess == value:
                print("Just right!")
                break
    except ValueError:
        pass
