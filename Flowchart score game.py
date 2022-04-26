import random
score = 10
def points(score):
    randomint = random.randint(10,15)
    userinput1 = int(input("Guess a number from 10 - 15: "))
    if userinput1 == randomint:
        score = score + 3
        print(randomint,"is the right number! You earn 3 points")
        print("your score right now is:",score)
        userinput = input("Do you want to go again?: ")
        if userinput == "yes":
            points(score)
        else:
            print("goodbye")
    elif userinput1 != randomint and 10 <= userinput1 <= 15:
        score = score - 1
        print(randomint,"was the correct number. Better luck next time")
        print("your score right now is:",score)
        userinput = input("Do you want to go again?: ")
        if userinput == "yes":
            points(score)
        else:
            print("goodbye")
    elif score == 0:
        print("you ran out of points")
    else:
        print("what are you doing")
        userinput2 = input("do you want to try again?(1 to play again, 0 to end): ")
        if userinput2 == "1":
            points(score)
        elif userinput2 =="0":
            print("goodbye")
points(score)
