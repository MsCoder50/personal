import tkinter 
from pytube import YouTube
from pytube import Playlist


root= tkinter.Tk()
def get_streams():
     
     
    download = YouTube(Link.get())
    streams = download.streams.all()
    vid= list(enumerate(streams))
    print(vid)
    # streams[3].download()
    tkinter.Label(text="Downloaded").pack()
    # tkinter.Button(text="Submit", command= get_value).pack()
    

root.geometry("800x800")

tkinter.Label(root,text="MS DODGER",pady=20).pack()

root.title("MS DODGER")

Link = tkinter.StringVar()

link= tkinter.Entry(root,textvariable=Link, font="Sans-serif 12").pack()

tkinter.Button(text="Submit",command=get_streams).pack()

root.mainloop()


