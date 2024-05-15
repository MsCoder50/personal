import tkinter as tk
import pywhatkit as ptkit

def make():
    txt= T.get("1.0","end-1c")
    ptkit.text_to_handwriting(txt,"Pyconverter.png")
    
    
root = tk.Tk()
root.geometry("1000x1000")
root.title("Text to handwriting")
T = tk.Text(root, height=43, width=30,bg="gray")
T.pack(fill="both")
T.insert(tk.END,"Enter your data")
tk.Button(text="Submit",bg="Gray", fg="black",relief="sunken",command=make).pack(pady=5)

tk.mainloop()