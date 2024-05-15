from tkinter import *
from geopy.geocoders import Nominatim
import geocoder
import mysql.connector
from tkinter import messagebox

root =Tk()

root.title("Track Status")
root.geometry("800x800")

try:
    conn= mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Hello@mscoder5",
    database="demo")

    cursor = conn.cursor()
except:
    messagebox.showerror("FIR","Sorry Server is currently closed please try in a few hours.")
    exit()
def check():
    
    Id_get = Id.get()
    print(Id_get)
    conn.commit()
    cursor.execute(f'''SELECT STATUS,Ph_no FROM {current_location} WHERE APPLICATION_ID = "{Id_get}" ''')
    detail = cursor.fetchall()
    Status=detail[0][0]
    Ph_no=detail[0][1]
    if Ph_no == None:
        Label(text=f"Application Status is {Status}").place(relx=0.5,rely=0.55,anchor=CENTER)
    else:
        Label(text=f"Application Status is {Status} and the Phone number of Police officer is {Ph_no}" ).place(relx=0.5,rely=0.55,anchor=CENTER)
try:
    Nomi_locator = Nominatim(user_agent="My App")

    my_location= geocoder.ip('me')


    latitude= my_location.geojson['features'][0]['properties']['lat']
                                
    longitude = my_location.geojson['features'][0]['properties']['lng']


    location = str(Nomi_locator.reverse(f"{latitude}, {longitude}"))


    locate= list(location.split(", "))
    current_location= locate[3].lower()
except:
    messagebox.showerror("FIR","Sorry we can't get your location Please Open your Internet to try again")
    exit()
    
Id = StringVar()

Label(text="Enter Your Application Id to see the Status: ").place(relx=0.5, rely=0.45, anchor=CENTER)
Entry(root,bd= 5, relief= GROOVE, textvariable= Id).place(relx=0.5,rely=0.5,anchor = CENTER)
Button(text="Submit",command=check).place(relx=0.63,rely=0.5,anchor = CENTER)

root.mainloop()