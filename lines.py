import sys

if len(sys.argv) < 2 or len(sys.argv) > 2:
    sys.exit("Invalid no of argument!")
if not sys.argv[1].endswith(".py"):
    sys.exit("File ERROR!")

try:
    with open(sys.argv[1], "r") as file:
        count = 0
        for row in file:
            row = row.strip()
            if row.startswith("#") or row == "":
                pass
            else:
                count += 1
except FileNotFoundError:
    print("File not found!!")

else:
    print(count)
