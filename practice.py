def main():
    x = get_value()


def get_value():
    while True :
        fraction = input("Fraction: ")
        x , y = fraction.split("/")

        try:
            x = int(x)
            y = int(y)
            if y == 0 :
                raise ZeroDivisionError

            elif not (y > 0):
                raise ValueError
            elif x > y:
                raise ValueError
            elif not (x >= 0):
                raise ValueError
            result = round((x/y)*100)        
        except ValueError:
            pass
        except ZeroDivisionError :
            pass
        # print(f"x is {x}.")
        # print(f"y is {y}.")
        else:
            if result <= 1:
                print("E")
            elif result >= 99:
                print("F")
            else:
                print(f"{result}%")
            break    


main()