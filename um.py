import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    match = re.findall(r"\bum\b",s,re.IGNORECASE)
    count = 0
    for m in match:
        count+=1
    return(count)



...


if __name__ == "__main__":
    main()

