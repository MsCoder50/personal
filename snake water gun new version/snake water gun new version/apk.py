import random
from tkinter import *

choices = ["s", "w" ,"g"]

plyrlife = 10

if plyrlife >0 :
        
    def snake() :
        global plyrlife
        plyrlife -= 1
        comp_choice = random.choice(choices)
        if comp_choice == "s":
            print("draw")
        elif comp_choice == "w":
            print("You win")
        elif comp_choice == "g":
            print("computer win")
            
    def water() :
        print("Hello world")
        
        
    def gun() :
        print("Hello world")
else:
    print("abhi lifes ni h")

root = Tk()

root.geometry("900x900")
root.title("SWG")
title_frame = Frame( padx = 5 , pady =10 )
title = Label(title_frame, text="Welcome to snake , water , gun Game" ,fg = "Black", borderwidth = 5 ,padx = 5 , pady= 5 )


scoreboard_frame = Frame( padx = 10, pady = 10 )
score = Label(scoreboard_frame , text="Score:-", padx = 50)

game_frame = Frame(root ,padx = 100, pady = 100 )
Snake = Button(game_frame , text = "Snake", borderwidth= 5, command = snake)
Water = Button(game_frame , text = "Water", borderwidth= 5, command = water)
Gun = Button(game_frame , text = "Gun",  borderwidth= 5, command = gun)


footer = Label(text="Powered by MS enterprises", bg = "Brown", fg = "White", padx ="450",pady="2", font="sans-serif 10 bold", relief =SUNKEN)
# packing variables

title.pack()
title_frame.pack(side = "top", fill = X)

footer.pack(side=BOTTOM ,anchor = "sw", fill =X)

scoreboard_frame.pack(side = "left", fill =  Y)
score.pack()

game_frame.pack()
Snake.pack(side= LEFT)
Water.pack(side= LEFT)
Gun.pack(side= LEFT)



root.mainloop()