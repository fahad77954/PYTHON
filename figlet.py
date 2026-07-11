import sys
import random
from pyfiglet import *


def main():
    figlet()


def figlet():
    if len(sys.argv) == 1:
        text = input("Input: ")
        font_list = FigletFont.getFonts()
        f = Figlet(font=random.choice(font_list))
        print(f.renderText(text))
    # #  if len(sys.argv)==1:
    # #       text = input ("Input: ")
    # #       random.choice(list)
    # # elif  (sys.argv[1] != "-f" and sys.argv[1] != "--font"):
    # #     sys.exit()
    # # elif len(sys.argv)==2:
    # #     sys.exit()
    # # elif len(sys.argv) == 3 and (sys.argv[1] != "-f" and sys.argv[1] != "--font"):
    #     sys.exit()

    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        font_list = FigletFont.getFonts()
        if sys.argv[2]  not in font_list :
              sys.exit(1)
        else:
            text = input("Input: ")
            f = Figlet(font=sys.argv[2])
            print(f.renderText(text))
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()

# how to use figlet
# f = Figlet(font='slant')
# print(f.renderText('text to render'))
