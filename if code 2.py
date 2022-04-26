#< is the right less than left
#<= is the right less than or equal to the left
#> is the right greater than left
#>= is the right greater than or equal left
#== Is the right euqal to left
    #== compares values
    #= assigns a value
#!= is the right not equal to the left

from cmath import pi
import math
import random

def mark(): #not part of the hw
    mark = int(input("Enter mark: "))
    if 90<=mark<=100:
        print("you have an A")
    elif 80<=mark<=90:
        print("you have a B")
    elif 70<=mark<=80:
        print("you have a C")
    elif 50<=mark<=70:
        print("you have a D")
    else:
        print("you are failing")

def doggame():
    Userage = int(input("How old are you?: "))
    dog = input("Do you have a dog?: ")
    if dog == "yes":
        dogage = int(input("How old is your dog?:"))
        dog = dogage*7
        if Userage > dog:
            print("You are older!")
        elif Userage == dog:
            print("You are the same age")
    else:
        dogeage = random.randint(1,10)
        dog = dogeage*7
        print("a random age has been chosen for your new dog! Your new dog's age is",dog)
        print("Your dog is older!")
        if Userage == dog:
            print("You are the same age")
    print("Goodbye")

def triangle():
    a = int(input("what is one side length (a): "))
    b = int(input("what is another side length (b): "))
    c = int(input("what is the last side length (c): "))
    if a**2 + b**2 == c**2:
        print("it is a right triangle")
    else:
        print("it is not a right triangle")

def aandb():
    a = int(input("pick a number for a: "))
    b = int(input("pick a number for b: "))
    addition = a+b
    multiplication = a*b
    if a>b:
        print("a + b =",addition)
    else:
        print("a x b =",multiplication)

def circle():
    r= int(input("put in the value for the radius: "))
    circumference = round(2*pi*r,1)
    area = round(pi*r**2,1)
    print("the circumference of the circle with the radius of",r,"is",circumference)
    print("the area of the circle with the radius of",r,"is",area)

def temperature():
    temperature = int(input("What is the temperature today?: "))
    cloudy = input("Is it cloudy today?: ")
    if temperature >= 20  and cloudy == "yes":
        print("Today is hot and cloudy")
    elif temperature >= 20 and cloudy == "no":
        print("Today is hot")
    elif 30 >= temperature >= 10 and cloudy == "yes":
        print("Today is warm and cloudy")
    elif 30 >= temperature >= 10 and cloudy == "no":
        print("Today is warm")
    elif 0 <= temperature <= 10 and cloudy == "yes":
        print("Today is cold and cloudy")
    elif 0 <= temperature <= 10 and cloudy == "no":
        print("Today is cold")
    elif temperature <= 0 and cloudy == "yes":
        print("Today is freezing and cloudy")
    elif temperature <= 0 and cloudy == "no":
        print("Today is freezing")
    else:
        print("I don't understand. Goodbye")

