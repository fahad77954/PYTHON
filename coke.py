def main ():
    amount_due = 50
    coke (amount_due)

def coke (amount_due):
    while amount_due > 0 :
        print(f"Amount Due : { amount_due} " )
        insert_coin = int(input("Insert coin : "))
        if insert_coin == 25 or insert_coin == 5 or insert_coin == 10 :
            amount_due-=insert_coin
        else:
           pass
    print(f"Change Owed : {amount_due*-1}")
main()