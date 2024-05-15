from tkinter import *
import sounddevice as sd
import soundfile as sf



    
def start():
    fs=48000
    dur= 10
    myrec = sd.rec(int(dur * fs),samplerate=fs,channels=2)
    sd.wait()
    return sf.write("My_Audio_file.mp3",myrec,fs)



root = Tk()

Button(text="Start",command= start).pack()

root.mainloop()