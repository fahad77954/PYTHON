import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search(r'src="https?://(?:www\.)?youtube\.com/embed/(?P<idno>(?:\w|-)+)"',s)
    if  matches :
         id =matches.group("idno")
         id=str(id)
         url="https://youtu.be/"+id
         return url
    else:
        return None     
if __name__ == "__main__":
    main()
