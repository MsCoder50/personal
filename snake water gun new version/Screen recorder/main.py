from tkinter import *
import pyscreenrec
import datetime

def play():
    # file= datetime.datetime.now()
    # print(file)
    rec.start_recording("file.mp4",10)
def stop():
    rec.stop_recording()
root= Tk()

rec = pyscreenrec.ScreenRecorder()

Button(text="Play",command=play).pack()
Button(text="stop",command=stop).pack()
root.mainloop()