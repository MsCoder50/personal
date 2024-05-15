from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Admin")
root.geometry("800x800")
def submit():
    
    username = u_name.get()
    password= pas.get()
    
    if username == "Admin" and password == "admin":
        root.destroy()
        import update
    else:
        messagebox.showerror("FIR","Invalid Username/Password")
    
u_name = StringVar()
pas= StringVar()
Label(text="Enter Username:").place(relx=0.35,rely=0.5,anchor=CENTER)
Entry(root,bd= 5, relief= GROOVE, textvariable= u_name).place(relx=0.5,rely=0.5,anchor = CENTER)
Label(text="Enter Password:").place(relx=0.35,rely=0.55,anchor=CENTER)
Entry(root,bd= 5, relief= GROOVE, textvariable= pas,show="*").place(relx=0.5,rely=0.55,anchor = CENTER)

Button(text="Submit",command=submit).place(relx=0.5,rely=0.6,anchor = CENTER)
root.mainloop()