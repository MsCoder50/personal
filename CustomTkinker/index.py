import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("CustomTkinter App")
root.geometry("500x500")

frame = customtkinter.CTkFrame(master=root)
frame.pack(padx=20,pady=20,fill="both",expand=True)

heading = customtkinter.CTkLabel(master=frame,text="Login",font=("Roboto", 20),pady=20)
heading.pack()

entry1= customtkinter.CTkEntry(master=frame,placeholder_text="Username",width=200)
entry1.pack(pady=(20,15))

entry2= customtkinter.CTkEntry(master=frame,placeholder_text="Password",show="*",width=200)
entry2.pack(pady=(0,15))

button= customtkinter.CTkButton(master=frame,text="Submit",width=100)
button.pack()

checkbox = customtkinter.CTkCheckBox(master=frame,text="Remember me")
checkbox.pack(pady=15,padx=10)
root.mainloop()