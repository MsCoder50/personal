import wmi
import time 
f = wmi.WMI()


lis =[]

    
while True:
    # time.sleep(0.2)
    for process in f.Win32_Process():
	    lis.append(process.name)
    if "Taskmgr.exe" in lis:
        print("Exit")
    else:
        print("Done")
    lis =[]
    