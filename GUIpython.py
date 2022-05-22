from cProfile import label
from fileinput import filename
import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []
#ensuring the file is saved

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

#making links work
#adding apps to our directory
def  Appname():
    
    for widget in frame.winfo_children():
        widget.destroy()


    filename=filedialog.askopenfilename(initialdir="/", title="Select file", 
                                        filetypes=(('executables', '.exe'), ('all files', '*.*')))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg='gray')
        label.pack()


def runApps():
    for app in apps:
        os.startfile(app)

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()


frame = tk.Frame(root, bg="white")
frame.place(relheight=0.9, relwidth=0.8, relx=0.1, rely=0.1)

#add buttons
openFile = tk.Button(root, text="Open file", padx=10, pady=6, fg="white", bg="#263D42", command=Appname)
openFile.pack()
runApps = tk.Button(root, text="Run Apps", padx=10, pady=6, fg="white", bg="#263D42", command=runApps)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()


root.mainloop()

#saves files whenever we close the application

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app+',')