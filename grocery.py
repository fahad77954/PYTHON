items = []
finallist = []

while True:
    try:
        item = input("")
    except EOFError:
        print()
        break
    else:
        items.append(item)

for i in items:
    a = i.upper()
    finallist.append(a)

finallist.sort()

for i in range(0, len(finallist)):
    A = 0
    for S in range(0, len(finallist)):
        if finallist[i] == finallist[S]:
            A += 1

    duplicate = False
    for z in range(0, i):
        if finallist[z] == finallist[i]:
            duplicate = True

    if duplicate == False:
        print(f"{A} {finallist[i]}")
