from tkinter import *
from tkinter.ttk import *

class SplashScreen(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        logo = PhotoImage(file="logo.png")
        logo_label = Label(self.master, image=logo)
        logo_label.image = logo
        logo_label.pack(side=TOP, pady=10)

        self.progress = Progressbar(self.master, orient="horizontal", length=400, mode="indeterminate")
        self.progress.pack(pady=10)

root = Tk()
app = SplashScreen(root)
root.mainloop()
