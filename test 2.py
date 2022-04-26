import random

print("Student: Joseph Baek")
print("Instructor: Ella Katsman")
print("ICS0")

randomnumber = random.randint(100,150) #getting a number frmo 100 - 150
hintnumber = random.randint(5,10) #getting a number to use for the hint
hintnumber1 = hintnumber + randomnumber #saving the hint numbers   
hintnumber2 = randomnumber - hintnumber #saving the hing numbers

points = 0 #points

print("Guess a number between 100 - 150")
hint = input("Do you want a hint?: ")
if hint == "yes": #if they say yes they get less points but they have a higher chance
    print("The number is inbetween",hintnumber1,"and",hintnumber2)
    guess = int(input("Answer: "))
    if guess == randomnumber:
        print("Correct! You got the number! You get 5 points for using a hint")
        points = points + 5
        print("You have",points,"points")
    elif randomnumber - 5 <= guess or randomnumber + 5 <= guess and randomnumber - 1 < guess:
        print("You were so close. You get 1 point for using a hint. The number was",randomnumber)
        points = points + 1
        print("You have",points,"points")
    elif randomnumber - 10 <= guess or randomnumber + 10 <= guess and randomnumber - 5 < guess:
        print("You were almost there. You don't get any points. The number was",randomnumber)
    elif randomnumber - 11 > guess or randomnumber + 11 > guess:
        print("You were not close at all. You don't get any points. The number was",randomnumber)
    elif guess < 100 or guess > 150:
        print("Not inbetween 100 and 150")
elif hint == "no": #if they say no then they get more points but its harder to get it right
    guess = int(input("Answer: "))
    if guess == randomnumber:
        print("Correct! You got the number! You get 10 points for not using a hint!")
        points = points + 10
        print("You have",points,"points")
    elif randomnumber - 5 <= guess or randomnumber + 5 <= guess and randomnumber - 1 < guess:
        print("You were so close. You get 5 points for trying without a hint. The number was",randomnumber)
        points = points + 5
        print("You have",points,"points")
    elif randomnumber - 10 <= guess or randomnumber + 10 <= guess and randomnumber - 5 < guess:
        print("You were almost there. You get 1 points for trying without a hint. The number was",randomnumber)
        points = points + 1
        print("You have",points,"points")
    elif randomnumber - 11 > guess or randomnumber + 11 > guess:
        print("You were not close at all. You don't get any points. The number was",randomnumber)
    elif guess < 100 or guess > 150:
        print("Not inbetween 100 and 150")
print("Goodbye")