a = int(input("what is one side length (a): "))
b = int(input("what is another side length (b): "))
c = int(input("what is the last side length (c): "))
if a**2 + b**2 == c**2:
    print("it is a right triangle")
else:
    print("it is not a right triangle")