


while True:
    def loop():
        import random
        num1 = float(random.randrange(-6,8)) #getting a random number from -6 to 8
        num2 = float(random.randrange(-6,8))
        answer = round((num1/num2),1)
        print("What is",num1,"/",num2,"?")
        userinput = float(input("Answer: "))
        if userinput == answer:
            print("correct")
        elif num2 == 0:
            print("the denominator was 0")
        else:
            print("wrong")
            print(answer)
            loop()
    loop()