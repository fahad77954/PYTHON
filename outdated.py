def main():
    outdated()
def outdated():
    dates = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        try:
            date = input("Date: ")
            date = date.strip()

            if date[0].isalpha():

                first_word = ""

                for i in date:
                    if i == " ":
                        break
                    first_word += i

                if first_word not in dates:
                    raise ValueError

                first, year = date.split(",")
                month_name, day = first.split(" ")

                day = int(day)
                if day < 1 or day > 31:
                    raise ValueError

                if month_name == "January":
                    month = "01"
                elif month_name == "February":
                    month = "02"
                elif month_name == "March":
                    month = "03"
                elif month_name == "April":
                    month = "04"
                elif month_name == "May":
                    month = "05"
                elif month_name == "June":
                    month = "06"
                elif month_name == "July":
                    month = "07"
                elif month_name == "August":
                    month = "08"
                elif month_name == "September":
                    month = "09"
                elif month_name == "October":
                    month = "10"
                elif month_name == "November":
                    month = "11"
                elif month_name == "December":
                    month = "12"

                day = str(day)
                if len(day) == 1:
                    day = "0" + day

                year = year.strip()

                print(f"{year}-{month}-{day}")
                break

            elif date[0].isdigit():

                month, day, year = date.split("/")

                month = int(month)
                day = int(day)

                if month < 1 or month > 12:
                    raise ValueError

                if day < 1 or day > 31:
                    raise ValueError

                month = str(month)
                day = str(day)

                if len(month) == 1:
                    month = "0" + month

                if len(day) == 1:
                    day = "0" + day

                print(f"{year}-{month}-{day}")
                break

            else:
                raise ValueError

        except (ValueError, IndexError):
            pass


if __name__ == "__main__":
    main()
