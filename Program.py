from myFunctions import *

name = ""
diff = 5

def menu():
    print("/******************************************\ ")
    print("|---JustAnotherTextBasedAdventureGam3000---|")
    print("\******************************************/\n")

    print("(m) Move")
    print("(o) Options")
    print("(q) Quit")
    print("\nType a number")
    ans = input("-> ").lower()
    if(ans == "m"):
        #move()
        print("Not yet implemented")
    elif(ans == "o"):
        options()
    elif(ans == "q"):
        exit()


def options():
    global name, diff
    print("/*******************\ ")
    print("|------Options------|")
    print("\*******************/\n")

    print("(n) Change name")
    print("(d) Set difficulty level")
    print("(b) Back")
    ans = input("-> ").lower()
    if(ans == "n"):
        print("Type a new name:")
        name = input("-> ")
    elif(ans == "d"):
        print("Set difficulty level (1 - Easy, 10 - Hard")
        diff = intInput("-> ", 1, 11)
    elif(ans == "b"):
        exit()


menu()