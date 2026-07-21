import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.search(r"^([\d]{1,3})\.([\d]{1,3})\.([\d]{1,3})\.([\d]{1,3})$",ip)
    if matches:
        for part in matches.groups():
            if len(part) > 1 and part[0] == "0":
                return False
        first,second,third,fourth=matches.groups()
        first = int (first)
        second = int (second)
        third = int (third)
        fourth = int (fourth)
        if 0 <= first <=255 and 0 <= second <=255 and 0 <= third <=255 and 0 <= fourth <=255 :
            return "True"
        else:
            return "False"
    else :
        return "False"

if __name__ == "__main__":
    main()

"""
Suppose:
matches.groups()

returns:
("192", "168", "001", "5")

This loop:

for part in matches.groups():

means:
- First, part = "192"
- Then, part = "168"
- Then, part = "001"
- Then, part = "5"

So, part contains only ONE part at a time,
not all four parts together.

len(part) > 1
checks the length of that one part.

Example:
part = "001"

len(part)      # 3
part[0]        # "0"

Since it has more than one digit and starts
with "0", it is invalid.

In simple words:
"Check each part of the IP address one by one."
"""
