from tkinter import *
from geopy.geocoders import Nominatim
import geocoder
import mysql.connector
from tkinter import messagebox
import datetime

root = Tk()

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

try:
    conn= mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Hello@mscoder5",
    database="demo")
    cursor = conn.cursor(buffered=True)
except:
    messagebox.showerror("FIR","Server currently closed please try again in a few hours")
    



cursor.execute("SHOW TABLES")
def give_tables():
    for table_name in cursor:
        States = list(table_name)
        return States
root.title("User FIR ")
root.geometry("800x800")

def FIR_SUBMIT():
    user_name= name.get()    
    complaint_get = complaint.get("1.0",END)  
    a= give_tables()
    if current_location in a:
        curtime = datetime.datetime.now()
        Insert = f'''INSERT INTO {current_location} (NAME,COMPLAINT,LOCATION,STATUS,DateTime) VALUES 
        ("{user_name}",'{complaint_get}','{location}','not confirmed','{curtime}');'''
        cursor.execute(Insert)
        conn.commit()
        cursor.execute(f'''SELECT APPLICATION_ID FROM {current_location} WHERE COMPLAINT ="{str(complaint_get)}" ''')
        Application_no = cursor.fetchone()
        messagebox.showinfo("FIR",f"Your Application is successfully Applied Your application number  is {Application_no}  to see the current Status go to Application status page ,Thank you.")
        
        
    elif current_location not in a:           
        make_table = f'''CREATE TABLE {current_location}(
        APPLICATION_ID INT NOT NULL AUTO_INCREMENT,
        NAME VARCHAR(100) NOT NULL,
        COMPLAINT VARCHAR(255) NOT NULL,
        LOCATION VARCHAR(100),
        STATUS VARCHAR(20),
        DateTime VARCHAR(50),
        Ph_no int(12),
        PRIMARY KEY(APPLICATION_ID)
        )'''    
        cursor.execute(make_table)
        curtime = datetime.datetime.now()
        Insert = f'''INSERT INTO {current_location} (NAME,COMPLAINT,LOCATION,STATUS,DateTime) VALUES 
        ("{user_name}",'{complaint_get}','{location}','not confirmed','{curtime}');'''
        cursor.execute(Insert)
    else:
         messagebox.showerror("FIR","Sorry we can't get your location Please Open your Internet to try again")
    


Label(text="Enter details for Apply")
name= StringVar()

Label(root, text="Your Name", font = "lucida 12 bold", padx = 50.5 , pady = 25 ).grid(row = 2, column = 1)
Label(root, text="Complaint in brief:", font = "lucida 12 bold", padx = 51,pady=25,).grid(row = 3, column = 1)

user= Entry(root,bd= 5, relief= GROOVE, textvariable= name)
user.grid(row = 2, column = 2,  padx= 50)

complaint= Text(root, width = 30, height = 10)
complaint.grid(row= 3, column = 2)


Button(root,text="Submit",command= FIR_SUBMIT).grid(row=3, column= 3,padx= 50)

root.mainloop()