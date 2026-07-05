def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check length
    if len(s) < 2 or len(s) > 6:
        return False

    # First two characters must be letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # No spaces or punctuation
    for c in s:
        if not c.isalnum():
            return False

    # Check numbers
    for i in range(len(s)):
        if s[i].isdigit():

            # First number cannot be 0
            if s[i] == "0":
                return False

            # Everything after the first number must also be numbers
            for j in range(i, len(s)):
                if s[j].isalpha():
                    return False

            return True

    # No numbers in the plate
    return True


main()
