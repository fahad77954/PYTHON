import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search(
        r'<iframe[^>]*src="https?://(?:www\.)?youtube\.com/embed/([\w-]+)"',
        s
    )

    if matches:
        return "https://youtu.be/" + matches.group(1)

    return None


if __name__ == "__main__":
    main()
