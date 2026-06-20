Question = input("what the Answer to the Great Question of Life, the Universe and Everything? ")
Question=Question.strip(" ")
match Question:
    case "42" | "forty-two" | "forty two"  | "FoRty TwO":
        print("Yes")
    case _:
        print("No")
