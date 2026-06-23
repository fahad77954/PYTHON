def main ():
    meal_time=input("Enter meal time:")
    c=convert(meal_time)
    if c>=7 and c <=8:
        print("breakfast time")
    elif c>=12 and c<=13 :
        print("lunch time")
    elif c>=18 and c<= 19 :
        print("dinner time")
def convert(m):
    first_part,second_part=m.split(":")
    first_part= int( first_part)
    second_part=int(second_part)
    time=first_part+(second_part/60)
    time=float(time)
    return time
if __name__ == "__main__":
    main()



