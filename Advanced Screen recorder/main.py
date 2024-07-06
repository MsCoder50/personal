from tkinter import *
import pyscreenrec
import sounddevice as sd
import soundfile as sf
import win32gui, win32con
import moviepy.editor as mpe

def play():
    if durtion=="":
        a = Label(text="Invalid Token ", background="black", fg="white", font="Arial 15")
        a.pack()
        root.update()
    else:
        Minimize= win32gui.GetForegroundWindow()
        win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)
        rec.start_recording("file.mp4",10)
        fs=44100
        dur= int(durtion.get())
        myrec = sd.rec(int(dur * fs),samplerate=fs,channels=2)
        sd.wait()
        return sf.write("record.mp3",myrec,fs)

def stop():
    rec.stop_recording()
root= Tk()

root.title("Screen Recorder")
root.geometry("400x550")
root.resizable(False,False)
root.config(bg="black")
rec = pyscreenrec.ScreenRecorder()

Label(text="Screen Recorder", bg="black",fg="White", font="Arial 15",pady= 20).pack()

Button(text="Play",command=play, width=100, height=5, background="Gray",fg="white", font= "Arial 15").pack(pady="5")
Button(text="stop",command=stop, width=100, height=5,background="Gray",fg="white",   font= "Arial 15").pack(pady="5")

durtion = StringVar()
entry = Entry(root,textvariable=durtion, width=100, font="Arial 15", bg="Black",borderwidth="7",relief=SUNKEN, fg="White").pack(pady=15)
root.mainloop()