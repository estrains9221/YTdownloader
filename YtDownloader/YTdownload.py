import tkinter as tk
from tkinter import ttk
import os
#config for window
root = tk.Tk()
root.title("YouTube Downloader")
root.config(bg="skyblue")
root.geometry("600x150+620+200")
#variables
URLSSS = str
Downloader = "Downloaded"

#fuctions
def downloadclick():
    global Downloader
    global URLSSS
    os.system("yt-dlp "+"-P "+Downloader+" "+ URLSSS)

def return_pressed(event):
    global URLSSS
    URLSSS=event.widget.get()
    label.config(text=event.widget.get())



#UI
button = tk.Button(root,text="Download", command=downloadclick,).pack(anchor='s',side='bottom',pady=10, fill="x", padx= 20)

label = tk.Label(root, text="Waiting For Youtube Video")
label.pack(pady=10)

tk.Label(root, text="Youtube URL Here").pack()
entry = tk.Entry(root)
entry.bind("<Return>", return_pressed)
entry.pack(padx=20,fill="x")
#idk
root.mainloop()