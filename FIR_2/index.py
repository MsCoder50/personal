from tkinter import *

def user():
    root.destroy()
    import user
def admin():
    root.destroy()
    import admin
def track():
    root.destroy()
    import track
    
    

root = Tk()
root.title("FIR")
root.geometry("800x800")
root.config(bg="black")

Button(text="New application",padx=5,pady=2,font="Kalinga 10 bold",command=user).place(relx=0.385, rely=0.5, anchor=CENTER)
Button(text="Admin",padx=5,pady=2,font="Kalinga 10 bold",command=admin).place(relx=0.5, rely=0.5, anchor=CENTER)
Button(text="Track Status",padx=5,pady=2,font="Kalinga 10 bold",command=track).place(relx=0.6, rely=0.5, anchor=CENTER)

root.mainloop()