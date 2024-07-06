import tkinter 
from pytube import YouTube
from pytube import Playlist


root= tkinter.Tk()
def get_streams():
    download = YouTube(Link.get())
    streams = download.streams.all()
    vid= list(enumerate(streams))
    get_streams.Sno = tkinter.StringVar()
    
    def get_value():
        values = int(get_streams.Sno.get())
        streams[values].download()
        # print("Downloaded")
        tkinter.Label(text="Downloaded").pack()
        
    for i in vid :
        tkinter.Label(text=i).pack()
        
    S_no = tkinter.Entry(textvariable=get_streams.Sno).pack()
    tkinter.Button(text="Submit", command= get_value).pack()
    

root.geometry("800x800")

tkinter.Label(root,text="PyDownloaer",pady=20).pack()

root.title("PyDownloader")

Link = tkinter.StringVar()

link= tkinter.Entry(root,textvariable=Link, font="Sans-serif 12").pack()

tkinter.Button(text="Submint",command=get_streams).pack()

root.mainloop()


