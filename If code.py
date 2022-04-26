#1
grade = int(input("what is your grade?: "))
if 100 >= grade >= 90:
    print("You are doing an excellent job!")
elif grade < 90:
   print("Continue to work hard")
elif 80 <= grade <= 90:
    print("Continue to work hard")
elif 50 <= grade < 80:
    print("You are passing")
elif 0 >= grade > 100:
    print("What do you mean your grade is greater than 100?")
elif grade < 0:
    print("What do you mean your grade is less than 0")
else:
    print("You are failing")

#2
number = int(input("Input a negative or positive number: "))
if number >= 0:
    print(number,"is positive")
else:
    print(number,"is negative")

#3
number = int(input("Pick a number: "))
if number%2 != 1:
    print(number,"is an even number")
else:
    print(number,"is an odd number")

#4
length = int(input("what is the length of the box: "))
height = int(input("what is the height of the box: "))
width = int(input("what is the width of the box: "))
if 0 < length*width*height < 1000:
    print("You are good to go")
elif length*width*height <= 0:
    print("What do you mean the box is 0 or less in cm3?")
else:
    print("This package is too big")

#5
import random
randomnumber = random.randint(-5,10)
if randomnumber < 0:
    print(randomnumber,"is negative")
elif randomnumber == 1 or randomnumber == 2 or randomnumber == 3 or randomnumber == 4:
    print(randomnumber)
else:
    print("the number is too big")

#6
age = int(input("How old are you?: "))
if age < 0:
    print("How is that possible?")
elif 0 <= age < 3:
    print("You are a Toddler")
elif 3 <= age < 10:
    print("You are a Child")
elif 10 <= age < 12:
    print("You are a PreTeen")
elif 12 <= age < 18:
    print("You are a Teenager")
else:
    print("You are an Adult")