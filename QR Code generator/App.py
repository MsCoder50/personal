from tkinter import * 
import qrcode as qr
# from PIL import Image
from tkinter import messagebox

def create_qr():
    get_link = link.get()
    get_version = ver_val.get()
    get_box = box_val.get()
    get_border = border_val.get()
    get_color = color_val.get()
    get_bgcolor= bgcolor_val.get()
    
    qr_code =qr.QRCode(version=get_version,error_correction=qr.constants.ERROR_CORRECT_H,box_size=get_box,border=get_border)
    qr_code.add_data(get_link)
    qr_code.make(fit=True)
    img = qr_code.make_image(fill_color=get_color,back_color=get_bgcolor)
    img.save("pyqr.png")
    messagebox.showinfo("QR code", "Your Qr Code has been saved in Directory of this application")
root = Tk()

root.title("QR Code Generator")
root.geometry("1000x1000")

root.config(bg='#0a0724')

Button(text="Exit",bg="Gray",font="Times 10 bold", command=exit,width=15,height=2).pack(side="top",anchor="e")

Label(root, text="Welcome to QR code generator",font="Times 20 bold",bg='#0a0724',fg='white').pack(pady=10)

Label(text="Enter Link or text:",bg="#0a0724",font="Times 15 bold italic",fg="white").pack(pady=15)
# Link taking

link = StringVar()
text = Entry(font="Times 13 bold", textvariable=link).pack(pady=5,padx=3)

# version 
Label(text="Version",bg="#0a0724",font="Times 10 bold italic",fg="white").pack(pady=5)
ver_val=StringVar()
options = list(range(1,21))
version = OptionMenu( root ,ver_val, *options )
version.pack(pady=5)


# box size
Label(text="Box size",bg="#0a0724",font="Times 10 bold italic",fg="white").pack(pady=5)
box_val=StringVar()
options_box = list(range(1,21))
box = OptionMenu( root ,box_val, *options_box )
box.pack(pady=5)


# border size
Label(text="Border size",bg="#0a0724",font="Times 10 bold italic",fg="white").pack(pady=5)
border_val=StringVar()
options_border = list(range(1,11))
border = OptionMenu( root ,border_val, *options_border )
border.pack(pady=5)


# Fill color
Label(text="Fill color",bg="#0a0724",font="Times 10 bold italic",fg="white").pack(pady=5)
color_val=StringVar()
options_color = ["Green", "Blue", "Orange", "Violet", "Red","Black","Gray","White" ,"Orange"]
color = OptionMenu( root ,color_val, *options_color )
color.pack(pady=5)

# Bg color
Label(text="Background color",bg="#0a0724",font="Times 10 bold italic",fg="white").pack(pady=5)
bgcolor_val=StringVar()
options_bgcolor = ["Green", "Blue", "Orange", "Violet", "Red","Black","Gray","White" ,"Orange"]
bgcolor = OptionMenu( root ,bgcolor_val, *options_bgcolor )
bgcolor.pack(pady=5)
# Submit button
Button(text="Submit",bg="Gray",fg="Black",font="Times 15 bold",relief=SUNKEN, command= create_qr).pack(pady=15)
root.mainloop()