from __future__ import unicode_literals
from tkinter import *
import tkinter as tk
import youtube_dl

win = tk.Tk()

win.title('Downloader')
win.geometry('500x200')
# Minimum size of the window
win.minsize(300, 300)
# Maximum size of the window
win.maxsize(600, 600)
win['bg'] = "blue"

# Enter the url - text field
txt = Entry(win, width=50)
txt.grid(column=0, row=3, sticky=W)


########################## Logic ######################################

# Getting the selection from the Radio Buttons
def sel():
    selection = str(var.get())
    return selection


# Downloading using the selected option
def download():
    selectionType = sel()
    if (selectionType == "audio"):
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }
    elif (selectionType == "bvideo"):
        ydl_opts = {
            'format': 'bestvideo + bestaudio',
            'outtmpl': '%(title)s.%(ext)s',
            'writesubtitles': True,
            'writeautomaticsub': True,
            'subtitleslangs': 'en',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4'
            }]
        }
    else:
        ydl_opts = {
            'format': 'best',
            'outtmpl': '%(title)s.%(ext)s',
            'writesubtitles': True,
            'writeautomaticsub': True,
            'subtitleslangs': 'en',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4'
            }]
        }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([txt.get()])


######################### View ##########################################

# Label
label = Label(win, text="Choose Option to Download", bg="blue")
label.grid(column=0, row=0)


# Radio buttons for selecting options
var = StringVar()
audio = Radiobutton(win, text="Audio", variable=var,
                    value="audio", activebackground="green", bg="blue", padx=3, command=sel)
audio.grid(column=0, row=2, sticky=W)

video = Radiobutton(win, text="BestVideo", variable=var,
                    value="bvideo", activebackground="green", bg="blue", padx=3, command=sel)
video.grid(column=0, row=2)

thumbnail = Radiobutton(win, text="NormalVideo",
                        variable=var, value="video", activebackground="green", bg="blue", command=sel)
thumbnail.grid(column=0, row=2, sticky=E)


# Download button
btn = Button(win, text="Download", fg="white", bg="blue",
             activebackground="green", command=download)
btn.grid(column=1, row=3)

########################################################################

win.mainloop()
