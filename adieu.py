import inflect
list_of_names = []
p = inflect.engine()
while True :
    try:
        name = input ("Name: ")
    except EOFError :
        break
    else :
        list_of_names.append(name)
print()
print(f"Adieu, adieu, to {p.join(list_of_names)}")
