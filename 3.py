grades = []
number = int(input("how many grades do you need to input?: "))
while number > 0:
    grade = int(input("what is the grade?: "))
    number = number - 1
    grades.append(grade)

if number == 0:
    average = sum(grades)/len(grades)
    print(sorted(grades))
    print("the average of the grades is:",average)
