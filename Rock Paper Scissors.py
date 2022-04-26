import random
import time

point = 3
def rps(point):
    computer = ["rock","paper","scissors"]
    comprandom = random.choice(computer)
    userinput = input("Rock, Paper, or Scissors?: ")
    if userinput == "Rock" and comprandom == "scissors":
        print("You went",userinput, "and the computer went . . .")
        time.sleep(3)
        print(comprandom)
        print("you win! You get 1 point!")
        point = point + 1
        print("you have",point,"points")
        userinput1 = input("do you want to play again?: ")
        if userinput1 == "yes":
            rps(point)
        else:
            print("have a good day")
    elif userinput == "Paper" and comprandom == "rock":
        print("You went",userinput, "and the computer went . . .")
        time.sleep(3)
        print(comprandom)
        print("you win! You get 1 point!")
        point = point + 1
        print("you have",point,"points")
        userinput1 = input("do you want to play again?: ")
        if userinput1 == "yes":
            rps(point)
        else:
            print("have a good day")
    elif userinput == "Scissors" and comprandom == "paper":
        print("You went",userinput, "and the computer went . . .")
        time.sleep(3)
        print(comprandom)
        print("you win! You get 1 point!")
        point = point + 1
        print("you have",point,"points")
        userinput1 = input("do you want to play again?: ")
        if userinput1 == "yes":
            rps(point)
        else:
            print("have a good day")
    elif userinput == "Rock" and comprandom == "rock" or userinput == "Paper" and comprandom == "paper" or userinput == "Scissors" and comprandom == "scissors":
        print("You went",userinput, "and the computer went . . .")
        time.sleep(3)
        print(comprandom)
        print("tie! You don't lose or a gain a point!")
        userinput1 = input("do you want to play again?: ")
        if userinput1 == "yes":
            rps(point)
        else:
            print("have a good day")
    else:
        print("You went",userinput, "and the computer went . . .")
        time.sleep(3)
        print(comprandom)
        print("you lost. You lose a point")
        point = point - 1
        if point == 0:
            print("you lost. No more points")
        print("you have",point,"points")
        userinput1 = input("do you want to play again?: ")
        if userinput1 == "yes":
            rps(point)
        else:
            print("have a good day")
rps(point)