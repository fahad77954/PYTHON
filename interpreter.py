exp=input("Enter the expression you want to evaluate:")
x,y,z=exp.split(" ")
x=int(x)
z=int(z)
a=0
if y== "+":
    a=x+z
    print(f"{a:.1f}")
elif y== "-":
    a=x-z
    print(f"{a:.1f}")
elif y== "*":
    a=x*z
    print(f"{a:.1f}")
elif y== "/" and z!=0:
    a=x/z
    print(f"{a:.1f}")
else:
    print("Invalid! Expression...")

