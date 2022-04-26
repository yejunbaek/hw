
equation = input("name your operation: ")
while equation == "x":
    def multiplication(x,y):
        print(x*y)
    multiplication(int(input("choose your first number: ")), int(input("choose your second number: ")))
while equation == "+":
    def addition(x,y):
        print(x+y)
    addition(int(input("choose your first number: ")),(int(input('choose your second number: '))))
while equation == "/":
    def division(x,y):
        print(x/y)
    division(int(input("choose your first number: ")),(int(input("choose your second number: "))))
while equation == "-":
    def subtraction(x,y):
        print(x-y)
    subtraction(int(input("choose your first number: ")),(int(input("choose your second number: "))))

if equation != int or float (""):
    print("what are you doing")
