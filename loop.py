import time
term = 5
int1 = int(input("What is your first number?: "))
int2 = int(input("What is your second number?: "))
print(int1)
print(int2)
while term > 0:
    int1 = int1+int2
    int2 = int1 + int1
    print(int1)
    term = term - 1
    time.sleep(1)
    print(int2)
    time.sleep(1)
    term = term - 1
