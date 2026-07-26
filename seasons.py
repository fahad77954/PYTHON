from datetime import date
import sys
import inflect


def main():
    try:
        birthday = date.fromisoformat(input("Date of birth: "))
    except ValueError:
        sys.exit("Invalid date")

    today = date.today()
    difference = today - birthday
    print(convert(difference.days))


def convert(days):
    p = inflect.engine()
    minutes = days * 24 * 60
    return p.number_to_words(minutes, andword="").capitalize() + " minutes"


if __name__ == "__main__":
    main()
