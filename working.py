import re
import sys


def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError as e:
        sys.exit(e)


def convert(s):
    pattern = r"^(?P<first>\d{1,2}(?::\d{2})? (?:AM|PM)) to (?P<second>\d{1,2}(?::\d{2})? (?:AM|PM))$"
    matches = re.search(pattern, s)

    if not matches:
        raise ValueError("ValueError")

    initial = matches.group("first")
    after = matches.group("second")

    # SITUATION 1: Both have colons
    if ":" in initial and ":" in after:
        h1, temp1 = initial.split(":")
        m1, p1 = temp1.split(" ")
        h2, temp2 = after.split(":")
        m2, p2 = temp2.split(" ")

    # SITUATION 2: Initial has colon, after does not
    elif ":" in initial and ":" not in after:
        h1, temp1 = initial.split(":")
        m1, p1 = temp1.split(" ")
        h2, p2 = after.split(" ")
        m2 = "00"

    # SITUATION 3: Initial has no colon, after does
    elif ":" not in initial and ":" in after:
        h1, p1 = initial.split(" ")
        m1 = "00"
        h2, temp2 = after.split(":")
        m2, p2 = temp2.split(" ")

    # SITUATION 4: Neither has a colon
    else:
        h1, p1 = initial.split(" ")
        m1 = "00"
        h2, p2 = after.split(" ")
        m2 = "00"

    int_h1, int_m1 = int(h1), int(m1)
    int_h2, int_m2 = int(h2), int(m2)

    # Validate ranges
    if not (1 <= int_h1 <= 12) or not (0 <= int_m1 <= 59):
        raise ValueError("ValueError")
    if not (1 <= int_h2 <= 12) or not (0 <= int_m2 <= 59):
        raise ValueError("ValueError")

    # Convert to 24-hour format (12 -> 0 via %12, then +12 if PM)
    int_h1 = int_h1 % 12
    if p1 == "PM":
        int_h1 += 12

    int_h2 = int_h2 % 12
    if p2 == "PM":
        int_h2 += 12

    return f"{int_h1:02}:{int_m1:02} to {int_h2:02}:{int_m2:02}"


if __name__ == "__main__":
    main()
