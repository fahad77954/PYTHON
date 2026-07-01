camel = input("Enter camelCase: ")
words = []
a = ""
for i in camel:
    if i.isupper():
        words.append(a)
        a = i.lower()
    else:
        a += i
words.append(a)
snake = "_".join(words)
print(snake)
