import random
while True:
        
    choices = ["s", "w", "g"]

    print("Welcome to Snake , water , gun Game")
    print(
        "Choose one of them :- s(snake) \n   \t\t      w(water) \n\t\t      g(Gun)")

    plyrlife = 10
    compwin = 0
    plyrwin = 0
    draw = 0
    invalid = 0
    while plyrlife > 0:

        plyrchoice = str(input("What yo've choosen:- "))
        comptchoice = random.choice(choices)
        plyrlife -= 1
        if comptchoice == "s" and plyrchoice == "w":
            compwin += 1
            print("Computer wins")
        elif comptchoice == "g" and plyrchoice == "s":
            compwin += 1
            print("Computer wins")
        elif comptchoice == "w" and plyrchoice == "g":
            compwin += 1
            print("Computer wins")
        elif comptchoice == "w" and plyrchoice == "s":
            plyrwin += 1
            print("You wins")
        elif comptchoice == "s" and plyrchoice == "g":
            plyrwin += 1
            print("You wins")
        elif comptchoice == "g" and plyrchoice == "w":
            plyrwin += 1
            print("You wins")
        elif comptchoice == "s" and plyrchoice == "s":
            draw += 1
            print("Draw")
        elif comptchoice == "g" and plyrchoice == "g":
            draw += 1
            print("Draw")
        elif comptchoice == "w" and plyrchoice == "w":
            draw += 1
            print("Draw")
        else:
            print("Invalid token")
            invalid += 1
    print("\n\n\n\t \t \t \t \t \t \t \t \t \t Game Results")
    print(
        "----------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    )
    print("\n \t \t \t \t \t \t \t \t \t Computer Wins:-", compwin)
    print("\n \t \t \t \t \t \t \t \t \t You Wins:-", plyrwin)
    print("\n\t \t \t \t \t \t \t \t \t Draw:-", draw)
    print("\n\t \t \t \t \t \t \t \t \t Invalid:-", invalid)

    if compwin > plyrwin:
        print(" \n\t \t \t \t \t \t \t   Finally Computer Wins beter Luck next time")
    elif plyrwin > compwin:
        print("\n\t \t \t \t \t \t \t \t   Hurray! You win")
    elif plyrwin == compwin:
        print("\n\t \t \t \t \t \t \t \t \t Draw ")
        
    