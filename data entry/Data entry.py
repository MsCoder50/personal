from tkinter import *

def add():
    name_val= name.get()
    dob_val= DOB.get()
    with open("log.txt","a") as file :
        file.write(f"Name is {name_val} and DOB is {dob_val}\n")
        Label(text="Thank you for coming with us").grid()
       
root = Tk()


root.geometry("900x900")

root.title("Add your name to go in party")

Label(root ,text ="Write your name please:-").grid()
Label(root ,text ="Write your DOB please:-").grid(row=1)

name = StringVar()
DOB = StringVar()

name_entry= Entry(root, textvariable = name)
DOB_entry= Entry(root, textvariable = DOB)



name_entry.grid(row = 0, column = 1)

DOB_entry.grid(row = 1, column = 1)




btn = Button(text = "Submit",command = add).grid(row = 2)


root.mainloop()