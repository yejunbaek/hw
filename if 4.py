
import random

print("Student: Joseph Baek, Mika") #names
print("Instructor: Ella Katsman") #teacher
print("ICS0") #class
print("Date: 03/29/22") #date

#Math

cont = True
points = 0
num1 = random.randrange(-6,8) #getting a random number from -6 to 8
num2 = random.randrange(-6,8) #getting another random number from -6 to 8


print("Question: ",num1,"+",num2,"= ?") #printing an addition question
userinput = int(input("Answer: ")) #getting user to put in the answer
while userinput != num1+num2:
    print("Wrong")
    print("Question: ",num1,"+",num2,"= ?") #printing an addition question
    userinput = int(input("Answer: "))
print("You have the correct answer. You gain a point!")
points = points + 1
print("You have",points,"points now!")
num1 = random.randrange(-6,8) #getting a random number from -6 to 8
num2 = random.randrange(-6,8) #getting another random number from -6 to 8


print("Question: ",num1,"x",num2,"= ?") #printing an addition question
userinput = int(input("Answer: ")) #getting user to put in the answer

while userinput != num1*num2:
        print("Wrong")
        print("Question: ",num1,"x",num2,"= ?") #printing an addition question
        userinput = int(input("Answer: "))
print("You have the correct answer. You gain a point!")
points = points + 1
print("You have",points,"points now!")
num1 = random.randrange(-6,8) #getting a random number from -6 to 8
num2 = random.randrange(-6,8)#getting another random number from -6 to 8


print("Question: ",num1,"^",num2,"= ?") #printing an addition question
userinput = float(input("Answer: ")) #getting user to put in the answer
square = num1**num2
while userinput != round(square,2):
    print("wrong")
    print(round(square,2))
    print("Question: ",num1,"^",num2,"= ?") #printing an addition question
    userinput = float(input("Answer: "))
print("You have the correct answer. You gain a point!")
points = points + 1
print("You have",points,"points now!")
num1 = float(random.randrange(-6,8)) #getting a random number from -6 to 8
num2 = float(random.randrange(-6,8)) #getting another random number from -6 to 8


print("Question: ",num1,"/",num2,"= ? (round to the 100th)") #printing an addition question
userinput = float(input("Answer: ")) #getting user to put in the answer
divide = num1/num2
while userinput != round(divide,2):
        print("Wrong")
        
        print("Question: ",num1,"/",num2,"= ?") #printing an addition question
        userinput = float(input("Answer: "))
print("You have the correct answer. You gain a point!")
points = points + 1
print("You have",points,"points now!")
num1 = float(random.randrange(-6,8)) #getting a random number from -6 to 8
num2 = float(random.randrange(-6,8))

print("Question: ",num1,"//",num2,"= ?") #printing an addition question
userinput = int(input("Answer: ")) #getting user to put in the answer
    
while userinput != num1//num2:
        print("Wrong")
        print("Question: ",num1,"//",num2,"= ?") #printing an addition question
        userinput = int(input("Answer: "))

print("You have the correct answer. You gain a point!")
points = points + 1
print("You have",points,"points now!")
num1 = float(random.randrange(-6,8)) #getting a random number from -6 to 8
num2 = float(random.randrange(-6,8))

print("Question: ",num1,"-",num2,"= ?") #printing an addition question
userinput = int(input("Answer: ")) #getting user to put in the answer
    
while userinput != num1 - num2:
    print("You are wrong")
    userinput = int(input("Answer: "))
print("You have the correct answer. You gain a point!")
points = points + 1
print("You have",points,"points now!")
num1 = float(random.randrange(-6,8)) #getting a random number from -6 to 8
num2 = float(random.randrange(-6,8))

print("Question: ",num1,"%",num2,"= ?") #printing an addition question
userinput = int(input("Answer: ")) #getting user to put in the answer
    
while userinput != num1%num2:
    print("You are wrong")
    userinput = int(input("Answer: "))
print("You have the correct answer. You gain a point!")
points = points + 1
print("You have",points,"points now!")
print("You have finished with",points,"/ 7 points!")
extra = input("Do you want to have an extra challenge? ")

if extra == 'Yes' or extra == 'yes':
    operation = ['+','-','/','*','%','**','//']
    randomoperation1 = random.choice(operation)
    randomoperation2 = random.choice(operation)
    num1 = random.randint(-6,8)
    num2 = random.randint(-6,8)
    num3 = random.randint(-6,8)
    print("Question:",num1,randomoperation1,num2,randomoperation2,num3,"= ?")
    while cont:
        if randomoperation1 == '+' and randomoperation2 == '-':
            userinput = int(input("Answer: "))
            if userinput == num1 + num2 - num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 + num2 - num3)+1 or userinput == (num1 + num2 - num3)-1:
                print("close")
                print("the right answer is",num1+num2-num3)
            else:
                print("wrong")
                print("the right answer is",num1+num2-num3)
        if randomoperation1 == '+' and randomoperation2 == '/':
            userinput = int(input("Answer: "))
            if userinput == num1 + num2 / num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 + num2 / num3)+1 or userinput == (num1 + num2 / num3)-1:
                print("close")
                print("the right answer is",num1+num2/num3)
            else:
                print("wrong")
                print("the right answer is",num1+num2/num3)
        if randomoperation1 == '+' and randomoperation2 == '*':
            userinput = int(input("Answer: "))
            if userinput == num1 + num2 * num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 + num2 * num3)+1 or userinput == (num1 + num2 * num3)-1:
                print("close")
                print("the right answer is",num1+num2*num3)
            else:
                print("wrong")
                print("the right answer is",num1+num2*num3)
        if randomoperation1 == '+' and randomoperation2 == '//':
            userinput = int(input("Answer: "))
            if userinput == num1 + num2  //num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 + num2 // num3)+1 or userinput == (num1 + num2 // num3)-1:
                print("close")
                print("the right answer is",num1+num2//num3)
            else:
                print("wrong")
                print("the right answer is",num1+num2//num3)
        if randomoperation1 == '+' and randomoperation2 == '**':
            userinput = int(input("Answer: "))
            if userinput == num1 + num2 ** num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 + num2 ** num3)+1 or userinput == (num1 + num2 ** num3)-1:
                print("close")
                print("the right answer is",num1+num2**num3)
            else:
                print("wrong")
                print("the right answer is",num1+num2**num3)
        if randomoperation1 == '+' and randomoperation2 == '%':
            userinput = int(input("Answer: "))
            if userinput == num1 + num2 % num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 + num2 % num3)+1 or userinput == (num1 + num2 % num3)-1:
                print("close")
                print("the right answer is",num1+num2%num3)
            else:
                print("wrong")
                print("the right answer is",num1+num2%num3)
        if randomoperation1 == '+' and randomoperation2 == '+':
            userinput = int(input("Answer: "))
            if userinput == num1 + num2 + num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 + num2 + num3)+1 or userinput == (num1 + num2 + num3)-1:
                print("close")
                print("the right answer is",num1+num2+num3)
            else:
                print("wrong")
                print("the right answer is",num1+num2+num3)

        if randomoperation1 == '-' and randomoperation2 == '+':
            userinput = int(input("Answer: "))
            if userinput == num1 - num2 + num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 - num2 + num3)+1 or userinput == (num1 - num2 + num3)-1:
                print("close")
                print("the right answer is",num1-num2+num3)
            else:
                print("wrong")
                print("the right answer is",num1-num2+num3)
        if randomoperation1 == '-' and randomoperation2 == '*':
            userinput = int(input("Answer: "))
            if userinput == num1 - num2 * num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 - num2 * num3)+1 or userinput == (num1 - num2 * num3)-1:
                print("close")
                print("the right answer is",num1-num2*num3)
            else:
                print("wrong")
                print("the right answer is",num1-num2*num3)
        if randomoperation1 == '-' and randomoperation2 == '**':
            userinput = int(input("Answer: "))
            if userinput == num1 - num2 ** num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 - num2 ** num3)+1 or userinput == (num1 - num2 ** num3)-1:
                print("close")
                print("the right answer is",num1-num2**num3)
            else:
                print("wrong")
                print("the right answer is",num1-num2**num3)
        if randomoperation1 == '-' and randomoperation2 == '/':
            userinput = int(input("Answer: "))
            if userinput == num1 - num2 / num3:
                print("correct! You get 3 points")
            elif userinput == (num1 - num2 / num3)+1 or userinput == (num1 - num2 / num3)-1:
                print("close")
                points = points + 3
                print("the right answer is",num1-num2/num3)
            else:
                print("wrong")
                print("the right answer is",num1-num2/num3)
        if randomoperation1 == '-' and randomoperation2 == '//':
            userinput = int(input("Answer: "))
            if userinput == num1 - num2 // num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 - num2 // num3)+1 or userinput == (num1 - num2 // num3)-1:
                print("close")
                print("the right answer is",num1-num2//num3)
            else:
                print("wrong")
                print("the right answer is",num1-num2//num3)
        if randomoperation1 == '-' and randomoperation2 == '%':
            userinput = int(input("Answer: "))
            if userinput == num1 - num2 % num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 - num2 % num3)+1 or userinput == (num1 - num2 % num3)-1:
                print("close")
                print("the right answer is",num1-num2%num3)
            else:
                print("wrong")
                print("the right answer is",num1-num2%num3)
        if randomoperation1 == '-' and randomoperation2 == '-':
            userinput = int(input("Answer: "))
            if userinput == num1 - num2 - num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 - num2 - num3)+1 or userinput == (num1 - num2 - num3)-1:
                print("close")
                print("the right answer is",num1-num2-num3)
            else:
                print("wrong")
                print("the right answer is",num1-num2-num3)

        if randomoperation1 == '*' and randomoperation2 == '+':
            userinput = int(input("Answer: "))
            if userinput == num1 * num2 + num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 * num2 + num3)+1 or userinput == (num1 * num2 + num3)-1:
                print("close")
                print("the right answer is",num1*num2+num3)
            else:
                print("wrong")
                print("the right answer is",num1*num2+num3)
        if randomoperation1 == '*' and randomoperation2 == '*':
            userinput = int(input("Answer: "))
            if userinput == num1 * num2 * num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 * num2 * num3)+1 or userinput == (num1 * num2 * num3)-1:
                print("close")
                print("the right answer is",num1*num2*num3)
            else:
                print("wrong")
                print("the right answer is",num1*num2*num3)
        if randomoperation1 == '*' and randomoperation2 == '**':
            userinput = int(input("Answer: "))
            if userinput == num1 * num2 ** num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 * num2 ** num3)+1 or userinput == (num1 * num2 ** num3)-1:
                print("close")
                print("the right answer is",num1*num2**num3)
            else:
                print("wrong")
                print("the right answer is",num1*num2**num3)
        if randomoperation1 == '*' and randomoperation2 == '/':
            userinput = int(input("Answer: "))
            if userinput == num1 * num2 / num3:
                print("correct! You get 3 points")
            elif userinput == (num1 * num2 / num3)+1 or userinput == (num1 * num2 / num3)-1:
                print("close")
                points = points + 3
                print("the right answer is",num1*num2/num3)
            else:
                print("wrong")
                print("the right answer is",num1*num2/num3)
        if randomoperation1 == '*' and randomoperation2 == '//':
            userinput = int(input("Answer: "))
            if userinput == num1 * num2 // num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 * num2 // num3)+1 or userinput == (num1 * num2 // num3)-1:
                print("close")
                print("the right answer is",num1*num2//num3)
            else:
                print("wrong")
                print("the right answer is",num1*num2//num3)
        if randomoperation1 == '*' and randomoperation2 == '%':
            userinput = int(input("Answer: "))
            if userinput == num1 * num2 % num3:
                print("correct! You get 3 points")
                points = points * 3
            elif userinput == (num1 * num2 % num3)+1 or userinput == (num1 * num2 % num3)-1:
                print("close")
                print("the right answer is",num1*num2%num3)
            else:
                print("wrong")
                print("the right answer is",num1*num2%num3)
        if randomoperation1 == '*' and randomoperation2 == '-':
            userinput = int(input("Answer: "))
            if userinput == num1 * num2 - num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 * num2 - num3)+1 or userinput == (num1 * num2 - num3)-1:
                print("close")
                print("the right answer is",num1*num2-num3)
            else:
                print("wrong")
                print("the right answer is",num1*num2-num3)

        if randomoperation1 == '**' and randomoperation2 == '+':
            userinput = int(input("Answer: "))
            if userinput == num1 ** num2 + num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 ** num2 + num3)+1 or userinput == (num1 ** num2 + num3)-1:
                print("close")
                print("the right answer is",num1**num2+num3)
            else:
                print("wrong")
                print("the right answer is",num1**num2+num3)
        if randomoperation1 == '**' and randomoperation2 == '*':
            userinput = int(input("Answer: "))
            if userinput == num1 ** num2 * num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 ** num2 * num3)+1 or userinput == (num1 ** num2 * num3)-1:
                print("close")
                print("the right answer is",num1**num2*num3)
            else:
                print("wrong")
                print("the right answer is",num1**num2**num3)
        if randomoperation1 == '**' and randomoperation2 == '**':
            userinput = int(input("Answer: "))
            if userinput == num1 ** num2 ** num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 ** num2 ** num3)+1 or userinput == (num1 ** num2 ** num3)-1:
                print("close")
                print("the right answer is",num1**num2**num3)
            else:
                print("wrong")
                print("the right answer is",num1**num2**num3)
        if randomoperation1 == '**' and randomoperation2 == '/':
            userinput = int(input("Answer: "))
            if userinput == num1 ** num2 / num3:
                print("correct! You get 3 points")
            elif userinput == (num1 ** num2 / num3)+1 or userinput == (num1 ** num2 / num3)-1:
                print("close")
                points = points + 3
                print("the right answer is",num1**num2/num3)
            else:
                print("wrong")
                print("the right answer is",num1**num2/num3)
        if randomoperation1 == '**' and randomoperation2 == '//':
            userinput = int(input("Answer: "))
            if userinput == num1 ** num2 // num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 ** num2 // num3)+1 or userinput == (num1 ** num2 // num3)-1:
                print("close")
                print("the right answer is",num1**num2//num3)
            else:
                print("wrong")
                print("the right answer is",num1**num2//num3)
        if randomoperation1 == '**' and randomoperation2 == '%':
            userinput = int(input("Answer: "))
            if userinput == num1 ** num2 % num3:
                print("correct! You get 3 points")
                points = points ** 3
            elif userinput == (num1 ** num2 % num3)+1 or userinput == (num1 ** num2 % num3)-1:
                print("close")
                print("the right answer is",num1**num2%num3)
            else:
                print("wrong")
                print("the right answer is",num1**num2%num3)
        if randomoperation1 == '**' and randomoperation2 == '-':
            userinput = int(input("Answer: "))
            if userinput == num1 ** num2 - num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 ** num2 - num3)+1 or userinput == (num1 ** num2 - num3)-1:
                print("close")
                print("the right answer is",num1**num2-num3)
            else:
                print("wrong")
                print("the right answer is",num1**num2-num3)

        if randomoperation1 == '/' and randomoperation2 == '+':
            userinput = int(input("Answer: "))
            if userinput == num1 / num2 + num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 / num2 + num3)+1 or userinput == (num1 / num2 + num3)-1:
                print("close")
                print("the right answer is",num1/num2+num3)
            else:
                print("wrong")
                print("the right answer is",num1/num2+num3)
        if randomoperation1 == '/' and randomoperation2 == '*':
            userinput = int(input("Answer: "))
            if userinput == num1 / num2 * num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 / num2 * num3)+1 or userinput == (num1 / num2 * num3)-1:
                print("close")
                print("the right answer is",num1/num2*num3)
            else:
                print("wrong")
                print("the right answer is",num1/num2**num3)
        if randomoperation1 == '/' and randomoperation2 == '**':
            userinput = int(input("Answer: "))
            if userinput == num1 / num2 ** num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 / num2 ** num3)+1 or userinput == (num1 / num2 ** num3)-1:
                print("close")
                print("the right answer is",num1/num2**num3)
            else:
                print("wrong")
                print("the right answer is",num1/num2**num3)
        if randomoperation1 == '/' and randomoperation2 == '/':
            userinput = int(input("Answer: "))
            if userinput == num1 / num2 / num3:
                print("correct! You get 3 points")
            elif userinput == (num1 / num2 / num3)+1 or userinput == (num1 / num2 / num3)-1:
                print("close")
                points = points + 3
                print("the right answer is",num1/num2/num3)
            else:
                print("wrong")
                print("the right answer is",num1/num2/num3)
        if randomoperation1 == '/' and randomoperation2 == '//':
            userinput = int(input("Answer: "))
            if userinput == num1 / num2 // num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 / num2 // num3)+1 or userinput == (num1 / num2 // num3)-1:
                print("close")
                print("the right answer is",num1/num2//num3)
            else:
                print("wrong")
                print("the right answer is",num1/num2//num3)
        if randomoperation1 == '/' and randomoperation2 == '%':
            userinput = int(input("Answer: "))
            if userinput == num1 / num2 % num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 / num2 % num3)+1 or userinput == (num1 / num2 % num3)-1:
                print("close")
                print("the right answer is",num1/num2%num3)
            else:
                print("wrong")
                print("the right answer is",num1/num2%num3)
        if randomoperation1 == '/' and randomoperation2 == '-':
            userinput = int(input("Answer: "))
            if userinput == num1 / num2 - num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 / num2 - num3)+1 or userinput == (num1 / num2 - num3)-1:
                print("close")
                print("the right answer is",num1/num2-num3)
            else:
                print("wrong")
                print("the right answer is",num1/num2-num3)

        if randomoperation1 == '//' and randomoperation2 == '+':
            userinput = int(input("Answer: "))
            if userinput == num1 // num2 + num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 // num2 + num3)+1 or userinput == (num1 // num2 + num3)-1:
                print("close")
                print("the right answer is",num1//num2+num3)
            else:
                print("wrong")
                print("the right answer is",num1//num2+num3)
        if randomoperation1 == '//' and randomoperation2 == '*':
            userinput = int(input("Answer: "))
            if userinput == num1 // num2 * num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 // num2 * num3)+1 or userinput == (num1 // num2 * num3)-1:
                print("close")
                print("the right answer is",num1//num2*num3)
            else:
                print("wrong")
                print("the right answer is",num1//num2**num3)
        if randomoperation1 == '//' and randomoperation2 == '**':
            userinput = int(input("Answer: "))
            if userinput == num1 // num2 ** num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 // num2 ** num3)+1 or userinput == (num1 // num2 ** num3)-1:
                print("close")
                print("the right answer is",num1//num2**num3)
            else:
                print("wrong")
                print("the right answer is",num1//num2**num3)
        if randomoperation1 == '//' and randomoperation2 == '/':
            userinput = int(input("Answer: "))
            if userinput == num1 // num2 / num3:
                print("correct! You get 3 points")
            elif userinput == (num1 // num2 / num3)+1 or userinput == (num1 // num2 / num3)-1:
                print("close")
                points = points + 3
                print("the right answer is",num1//num2/num3)
            else:
                print("wrong")
                print("the right answer is",num1//num2/num3)
        if randomoperation1 == '//' and randomoperation2 == '//':
            userinput = int(input("Answer: "))
            if userinput == num1 // num2 // num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 // num2 // num3)+1 or userinput == (num1 // num2 // num3)-1:
                print("close")
                print("the right answer is",num1//num2//num3)
            else:
                print("wrong")
                print("the right answer is",num1//num2//num3)
        if randomoperation1 == '//' and randomoperation2 == '%':
            userinput = int(input("Answer: "))
            if userinput == num1 // num2 % num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 // num2 % num3)+1 or userinput == (num1 // num2 % num3)-1:
                print("close")
                print("the right answer is",num1//num2%num3)
            else:
                print("wrong")
                print("the right answer is",num1//num2%num3)
        if randomoperation1 == '//' and randomoperation2 == '-':
            userinput = int(input("Answer: "))
            if userinput == num1 // num2 - num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 // num2 - num3)+1 or userinput == (num1 // num2 - num3)-1:
                print("close")
                print("the right answer is",num1//num2-num3)
            else:
                print("wrong")
                print("the right answer is",num1//num2-num3)

        if randomoperation1 == '%' and randomoperation2 == '+':
            userinput = int(input("Answer: "))
            if userinput == num1 % num2 + num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 % num2 + num3)+1 or userinput == (num1 % num2 + num3)-1:
                print("close")
                print("the right answer is",num1%num2+num3)
            else:
                print("wrong")
                print("the right answer is",num1%num2+num3)
        if randomoperation1 == '%' and randomoperation2 == '*':
            userinput = int(input("Answer: "))
            if userinput == num1 % num2 * num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 % num2 * num3)+1 or userinput == (num1 % num2 * num3)-1:
                print("close")
                print("the right answer is",num1%num2*num3)
            else:
                print("wrong")
                print("the right answer is",num1%num2**num3)
        if randomoperation1 == '%' and randomoperation2 == '**':
            userinput = int(input("Answer: "))
            if userinput == num1 % num2 ** num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 % num2 ** num3)+1 or userinput == (num1 % num2 ** num3)-1:
                print("close")
                print("the right answer is",num1%num2**num3)
            else:
                print("wrong")
                print("the right answer is",num1%num2**num3)
        if randomoperation1 == '%' and randomoperation2 == '/':
            userinput = int(input("Answer: "))
            if userinput == num1 % num2 / num3:
                print("correct! You get 3 points")
            elif userinput == (num1 % num2 / num3)+1 or userinput == (num1 % num2 / num3)-1:
                print("close")
                points = points + 3
                print("the right answer is",num1%num2/num3)
            else:
                print("wrong")
                print("the right answer is",num1%num2/num3)
        if randomoperation1 == '%' and randomoperation2 == '//':
            userinput = int(input("Answer: "))
            if userinput == num1 % num2 // num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 % num2 // num3)+1 or userinput == (num1 % num2 // num3)-1:
                print("close")
                print("the right answer is",num1%num2//num3)
            else:
                print("wrong")
                print("the right answer is",num1%num2//num3)
        if randomoperation1 == '%' and randomoperation2 == '%':
            userinput = int(input("Answer: "))
            if userinput == num1 % num2 % num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 % num2 % num3)+1 or userinput == (num1 % num2 % num3)-1:
                print("close")
                print("the right answer is",num1%num2%num3)
            else:
                print("wrong")
                print("the right answer is",num1%num2%num3)
        if randomoperation1 == '%' and randomoperation2 == '-':
            userinput = int(input("Answer: "))
            if userinput == num1 % num2 - num3:
                print("correct! You get 3 points")
                points = points + 3
            elif userinput == (num1 % num2 - num3)+1 or userinput == (num1 % num2 - num3)-1:
                print("close")
                print("the right answer is",num1%num2-num3)
            else:
                print("wrong")
                print("the right answer is",num1%num2-num3)
            cont = False 
    if points < 7:
        print("you have finished with",points,"/ 7 points")
        print("Goodbye")
    elif points > 7:
        print("you have finished with",points,"/ 10 points")
        print("Goodbye")
        