
import random
import time

pokeball = 10
storage = []
loop = True
catch1 = 1
fail = 2
def homescreen(storage):
    print("Storage")
    print("Battle")
    print("Shop")
    userinput = input("what would you like to do?: ")
    if userinput == "Battle" or userinput == "battle":
        print("Heading back into the wild . . .")
        time.sleep(3)
        wild(pokeball,catchorfail)
    elif (userinput == 'Storage') or userinput == 'storage':
        print(storage)
        homescreen(storage)
    else:
        homescreen(storage)

def pikachu(pokeball,loop,storage,randomcatch):
    while pokeball > 0:
        if randomcatch == catch1 and loop == True:
            pokeball = pokeball - 1
            print("caught!")
            print(pokeball,"pokeballs left")
            loop = False
            storage = "\n" "Pikachu" "\n"
        elif randomcatch == fail and loop == True:
            print("Fail")
            pokeball = pokeball - 1
            print(pokeball,"pokeballs left")
            catchagain = input("do you want to try again?: ")
            if catchagain == "yes" and pokeball > 0:
                pikachu(pokeball,loop,storage,randomcatch)
            else:
                homescreen(storage)
        elif pokeball == 0:
            loop = False
            print("You have no more pokeballs . . .")
            time.sleep(3)
            homescreen(storage)
        else:
            continueplaying = input("do you want to continue?: ")
            if continueplaying == "yes":
                wild(pokemon,catchorfail)
            else:
                print("returning home")
                time.sleep(3)
                homescreen(storage)            

        

pokemon = ["Pikachu","Evee","Magikarp"]
catchorfail = ["catch","fail"]
def wild(pokeball,catchorfail):
    random_pokemon = random.choice(pokemon)
    print("you have encountered a wild",random_pokemon)
    if random_pokemon == "Pikachu":
            catch = input("do you want to catch this pokemon?: ")
            print("you have",pokeball,"pokeballs left")
            if catch == "yes":
                randomcatch = random.choice(catchorfail)
                pikachu(pokeball,loop,storage,randomcatch)
            elif catch == "no":
                homescreen(storage)
wild(pokeball,catchorfail)

homescreen1 = input("do you want to show the home screeen?: ")
if homescreen1 == "yes":
    homescreen(storage)
homescreen(storage)


