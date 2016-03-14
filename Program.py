from myFunctions import * #import some useful functions I created for taking an integer input and displaying text in the center of the console
#Create player name and difficulty variables
name = ""
diff = 5

def menu(): #The main menu
    printCenter("TEXT ADVENTURE GAME")

    print("(m) Move") #Show th eplayer options
    print("(o) Options")
    print("(q) Quit")
    print("\nType a number")
    ans = input("-> ").lower() #Take user prompt, if the user inputs an unrecognised string it will return to the main menu
    if(ans == "m"):
        #move()
        print("Not yet implemented")
    elif(ans == "o"):
        options()
    elif(ans == "q"):
        exit()


def options(): #Show options to change player settings
    global name, diff #Allow changing global variables
    printCenter("OPTIONS")

    print("(n) Change name") #Show prompt
    print("(d) Set difficulty level")
    print("(b) Back")
    ans = input("-> ").lower() #Take input and make lowercase, less code in IF statement
    if(ans == "n"):
        print("Type a new name:")
        name = input("-> ")
    elif(ans == "d"):
        print("Set difficulty level (1 - Easy, 10 - Hard")
        diff = intInput("-> ", 1, 11)
    elif(ans == "b"):
        exit()


menu()
