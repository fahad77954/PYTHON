# THE MAIN FUNCTION WHERE THE USER INPUT THE TEXT
def main ():
    i=input("Enter the text: ")
    convert(i)
# CONVERTS THE TEXT
def convert(str):
    str = str.replace(":)","🙂")
    str = str.replace(":(","🙁")
    print(str)
# CALLS THE MAIN FUN
main()








