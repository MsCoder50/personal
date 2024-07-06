import customtkinter
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Hello@mscoder5",
        database="news")

    cursor = conn.cursor()
except:
    messagebox.showerror("News","Database Is Not Responding Please Come Back In a Few Hours.")
    exit()
    
root = customtkinter.CTk()
root.geometry("1200x700")
root.title("News")
def Signup(event):
    root.destroy()
    import signup
def Login():
    Username = entry1.get()
    Password = entry2.get()
    # print(f"Login Credentials: Username is{Username} and Password is {Password}")
    if Username == "" or Password == "":
        messagebox.showerror("News","Username or password could not be empty")

frame = customtkinter.CTkFrame(master=root)
frame.pack(padx=20,pady=20,fill="both",expand=True)

img = ImageTk.PhotoImage(Image.open("Assets/logo.jpg"))
logo = customtkinter.CTkLabel(master=frame,text="", image = img)
logo.pack(pady=(100,10))


heading = customtkinter.CTkLabel(master=frame,text="Login",font=("cascadia code", 20),pady=20)
heading.pack()

 

entry1= customtkinter.CTkEntry(master=frame,placeholder_text="Username",width=200)
entry1.pack(pady=(20,15))

entry2= customtkinter.CTkEntry(master=frame,placeholder_text="Password",show="*",width=200)
entry2.pack(pady=(0,15))

button= customtkinter.CTkButton(master=frame,text="Submit",width=200,command=Login)
button.pack()

checkbox = customtkinter.CTkCheckBox(master=frame,text="I accept all Terms and conditions")
checkbox.pack(pady=15,padx=10)

SignUp_text = customtkinter.CTkLabel(master= frame,text="Not a Member Yet. Click Here To Register")
SignUp_text.pack()
SignUp_text.bind('<Button-3>',Signup)
# customtkinter.CTkButton(master=frame,text="Login").pack()
root.mainloop()