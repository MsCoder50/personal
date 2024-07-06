from tkinter import *
from tkinter import messagebox
from geopy.geocoders import Nominatim
import geocoder
import mysql.connector

root = Tk()

conn= mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Hello@mscoder5",
    database="fir",
    # charset = 'utf8'
)

cursor = conn.cursor()

def mouseClick(event):
    canvas.destroy()
    adminframe.destroy()
    
    def FIR_SUBMIT():
        pass

    Nomi_locator = Nominatim(user_agent="My App")

    my_location= geocoder.ip('me')

    
    latitude= my_location.geojson['features'][0]['properties']['lat']
                                
    longitude = my_location.geojson['features'][0]['properties']['lng']

    
    location = Nomi_locator.reverse(f"{latitude}, {longitude}")
    

    
    
    
    Label(text="Enter details for Apply")
    name= StringVar()

    Label(root, text="Your Name", font = "lucida 12 bold", padx = 50.5 , pady = 25 ).grid(row = 2, column = 1)
    Label(root, text="Complaint in brief:", font = "lucida 12 bold", padx = 51,pady=25,).grid(row = 3, column = 1)

    user= Entry(root,bd= 5, relief= GROOVE, textvariable= name)
    user.grid(row = 2, column = 2,  padx= 50)

    complaint= Text(root, width = 30, height = 10)
    complaint.grid(row= 3, column = 2)
    input = complaint.get("1.0",END)
    
    Button(root,text="Submit",command= FIR_SUBMIT).grid(row=3, column= 3,padx= 50)

def submit():
    userval = str(username.get())
    pasval = str(password.get())
    
    if userval == "ADMIN" and pasval == "ROOT": 
        messagebox.showinfo("FIR","Thank you ")
        canvas.destroy()
        adminframe.destroy()
    elif userval == "" or password == "":
        messagebox.showerror("FIR","Blank not acceptable")
    else:
        messagebox.showerror("FIR","Invalid username/password")


root.title("FIR")
 
root.geometry("1400x900")

bg = PhotoImage(file="images/landscape.png")
  

canvas = Canvas( root, width = 1800,
                 height = 1000)
  
canvas.pack(fill = "both", expand = True)


canvas.create_image( 0, 0, image = bg, 
                     anchor = "nw") 
adminframe= Frame(root,bg = "grey", width= 500 , height= 400, borderwidth=10, relief=GROOVE)
adminframe.place(x= 500 ,y=200)


username= StringVar()
password= StringVar()

Label(adminframe, text="Username:", font = "lucida 12 bold", padx = 50.5 , bg= "grey",pady = 25 ).grid(row = 2, column = 1)
Label(adminframe, text="Password:", font = "lucida 12 bold", padx = 51, bg= "grey",pady=25).grid(row = 3, column = 1)

user= Entry(adminframe,bd= 5, relief= GROOVE, textvariable= username)
user.grid(row = 2, column = 2,  padx= 50)

pas= Entry(adminframe,bd= 5, relief= GROOVE, show = "*", textvariable= password)
pas.grid(row = 3, column = 2, padx= 50)

Button(adminframe, text="Submit", command = submit, bd= 5, relief= GROOVE, ).grid(row= 3, column = 3, padx=25 )
label = Label(adminframe, text="Wanna Apply for FIR Click here",bg= "grey")
label.grid(row= 4, column = 2)
label.bind("<Button-1>", mouseClick)
root.mainloop()