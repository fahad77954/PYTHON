import tabulate
import csv
import sys

if len(sys.argv) < 2  :
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2 :
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
list = []
try:
    with open (sys.argv[1],"r") as file :
        reader = csv.reader(file)
        for line in reader :
            list.append(line)

except FileNotFoundError:
    sys.exit(1)


# print(list)
print(tabulate.tabulate(list,headers="firstrow",tablefmt="grid"))
