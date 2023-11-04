from __future__ import unicode_literals
from tkinter import *
import tkinter as tk
import youtube_dl
import os
from tkinter import filedialog, ttk

win = tk.Tk()

win.title("Downloader")
win.geometry("500x200")
# Minimum size of the window
win.minsize(300, 300)
# Maximum size of the window
win.maxsize(600, 600)
win["bg"] = "blue"


# Enter the url - text field
txt = Entry(win, width=50)
txt.grid(column=0, row=6, sticky=W)

################ Logic ######################


# Getting the destination folder
def getdir():
    savedir = filedialog.askdirectory()
    os.chdir(savedir)
    dirpath = os.path.basename(os.getcwd())
    save_path = dirpath
    destination_display_label.config(text="Destination Folder = " + save_path)


# Getting the selection from the radio buttons
def sel():
    selection = str(var.get())
    return selection


# Downloading using the selected option
def download():
    selectionType = sel()
    if selectionType == "audio":
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": "%(title)s.%(ext)s",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
    elif selectionType == "bvideo":
        ydl_opts = {
            "format": "bestvideo + bestaudio",
            "outtmpl": "%(title)s.%(ext)s",
            "postprocessors": [
                {"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}
            ],
        }
    else:
        ydl_opts = {"format": "best", "outtmpl": "%(title)s.%(ext)s"}

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([txt.get()])


######################## View ################################

# label
label = Label(
    win, text="Choose Option to Download", bg="blue", font=("arial", 10, "bold")
)
label.grid(column=0, row=0)

# Radio buttons for selecting options
var = StringVar()
audio = Radiobutton(
    win,
    text="Audio",
    variable=var,
    value="audio",
    activebackground="green",
    bg="blue",
    padx=3,
    font=("arial", 10, "bold"),
    command=sel,
)
audio.grid(column=0, row=2, sticky=W)

video = Radiobutton(
    win,
    text="BestVideo",
    variable=var,
    value="bvideo",
    activebackground="green",
    bg="blue",
    padx=3,
    font=("arial", 10, "bold"),
    command=sel,
)
video.grid(column=0, row=2)

nvideo = Radiobutton(
    win,
    text="NormalVideo",
    variable=var,
    value="video",
    activebackground="green",
    bg="blue",
    padx=3,
    font=("arial", 10, "bold"),
    command=sel,
)
nvideo.grid(column=0, row=2, sticky=E)

# Browse Label
browse_label = Label(
    win, text="Choose Download Folder", bg="blue", font=("arial", 10, "bold")
)
browse_label.grid(column=0, row=3)

# Browse button
btn = ttk.Button(win, text="Browse", command=lambda: getdir())
btn.grid(column=0, row=4)

# Destination label
destination_display_label = Label(win, bg="blue", font=("arial", 10, "bold"))
destination_display_label.grid(column=0, row=5)

# Download button
btn = Button(
    win,
    text="Download",
    fg="white",
    bg="blue",
    activebackground="green",
    command=download,
)
btn.grid(column=1, row=6)

###############################################################

win.mainloop()
