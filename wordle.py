import random
words = ["CRANE"]
randomwords = random.choice(words)
print("Guess to guess the word! It's always a 5 letter word!")
userinput = input("Word: ")
if userinput == words[0] and userinput != words[1] and userinput != words[2] and userinput != words[3] and userinput != words[4]:
    print("? X X X X")
else:
    print("what")