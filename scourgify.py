import sys
import csv
import tabulate

# Too check length of command-line-arguments
if len(sys.argv) < 3:
    sys.exit("Too few argument")
if len(sys.argv) > 3:
    sys.exit("Too many argument")
# opening both before and after csv files
with open(sys.argv[1], "r") as file, open(sys.argv[2], "w") as file2:
    # a reader object of before file
    reader = csv.DictReader(file)
    # a writer object of after file and also specify column names for the after.csv file
    writer = csv.DictWriter(file2, fieldnames=["first", "last", "house"])
    # writing the header to the after.csv file
    writer.writeheader()
    # line is a dictionary of each line with key and value pair
    for line in reader:
        # getting the bvalue of the name key in dictionary
        name = line["name"]
        # split into two parts firstname and lastname
        last, first = name.split(",")
        # strip the spaces
        first = first.lstrip()
        # writing each row to the after.csv file
        writer.writerow({"first": first, "last": last, "house": line["house"]})

    # writer = csv.DictWriter(file2,fieldnames=["first","last","house"])
    # writer.writeheader()
    # for row in reader :
    #     name = row ["name"]
    #     last,first=name.split(",")
    #     first = first.lstrip()
    #     writer.writerow({"first": first ,  "last" :last ,"house" : row["house"] })
