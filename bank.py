money=0
greeting=input("Greeting:")
greeting=greeting.strip()
greeting=greeting.lower()
if "hello" in greeting :
    print(f"${money}")
elif "h" in greeting[0]:
    money=20
    print(f"${money}")
else:
    money=100
    print(f"${money}")
