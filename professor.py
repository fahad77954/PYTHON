import random


def main():
    level = get_level()
    equation = 0
    result = 0
    while equation < 10:
        x = generate_integer(level)
        y = generate_integer(level)

        z = x + y
        chance = 0
        while chance < 3:
            try:
                if chance == 0:
                    answer = int(input(f"{x} + {y} = "))
                    if answer == z:
                        result += 1
                        break
                    else:
                        chance += 1
                        raise ValueError
                else:
                    answer = int(input(f"{x} + {y} = "))
                    if answer == z:
                        result += 1
                        break
                    else:
                        chance += 1
                        raise ValueError
            except ValueError:
                print("EEE")
        if chance == 3:
            print(f"{x} + {y} = {z}")
        equation += 1
    print(f"Score: {result}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
            else:
                raise ValueError
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()
