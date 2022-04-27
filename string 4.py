

#userinput = input("Enter a string with at least 2 characters: ")

userinput = "Exit"
while userinput != "Exit":
    while len(userinput) < 2:
        userinput = input("Enter a string with at least 2 characters: ")
    print(userinput[-2:]*5)
    userinput = input("Enter a string with at least 2 characters: ")
print("Goodbye")

#userinput = input("Enter a string with at least 2 characters: ")
userinput = "Exit"
while userinput != "Exit":
    while len(userinput) < 2:
        userinput = input("Enter a string with at least 2 characters: ")
        userinput = userinput.replace(" ","_")
        print(userinput)
    userinput2 = input("Enter a string with 4 characters: ")
    while len(userinput2) > 4 or len(userinput2) < 4:
        userinput2 = input("Enter a string with 4 characters: ")
        userinput2 = userinput2.replace(" ","_")
        print(userinput2)
    userinput = input("Enter a string with at least 2 characters: ")
print("Goodbye")

userinput = "Exit"
#userinput = input("Enter a string with at least 2 characters: ")
while userinput != "Exit":
    while len(userinput) < 2:
        userinput = input("Enter a string with at least 2 characters: ")
    userinput2 = input("Enter a string with 4 characters: ")
    #cape
    while len(userinput2) > 4 or len(userinput2) < 4 or userinput2 != userinput2[0:2]+userinput2[1]+userinput2[0]:    
        userinput2 = input("Enter a string with 4 characters: ")
    userinput = input("Enter a string with at least 2 characters: ")
print("Goodbye")

userinput = input("Enter a string with at least 2 characters: ")
while userinput != "Exit":
    while len(userinput) < 2:
        userinput = input("Enter a string with at least 2 characters: ")
    userinput = userinput.replace(" ","_")
    userinput2 = input("Enter a string with 4 characters: ")
    while len(userinput2) > 4 or len(userinput2) < 4 or userinput2 != userinput2[0:2]+userinput2[1]+userinput2[0]:  
        userinput2 = input("Enter a string with 4 characters: ")
    userinput2 = userinput2.replace(" ","_")
    length = len(userinput2)//2
    print("Combined string:",userinput2[:length]+userinput[-2]+userinput[-1]+userinput2[length:])
    userinput = input("Enter a string with at least 2 characters: ")
print("Goodbye")