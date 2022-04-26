#a = "Enter 1st word: "
#b = "Enter 2nd word: "
#userinput = input(a)
#userinput2 = input(b)
#while userinput != userinput2:
#    print("if",userinput,"!=",userinput2,":")
#    print("    print(“Play Again”)")
#    print("else:")
#    print("    print(“Goodbye”)")
#    userinput = input(a)
#    userinput2 = input(b)
#print(userinput,"==",userinput2)
#print("Goodbye")




#a = "Enter 1st word: "
#b = "Enter 2nd word: "
#userinput = input(a)
#if userinput == "Exit":
#    print("Goodbye")
#userinput2 = input(b)
#if userinput2 == "Exit":
#    print("Goodbye")
#while not (userinput == "Exit" or userinput2 == "Exit"):
#    userinput = userinput[1:]
#    userinput2 = userinput2[1:]
#    print(userinput.capitalize()+userinput2)
#    userinput = input(a)
#    if userinput == "Exit":
#        break
#    userinput2 = input(b)
#    if userinput2 == "Exit":
#        break
#print("Goodbye")

word1 = input("Enter a words 4 at least 4 characters long: ")
while word1 != "end":
    print(str.capitalize(word1[2: 5] + word1[0:2] + word1[5:]))
    word1 = input("Enter a words 4 at least 4 characters long: ")