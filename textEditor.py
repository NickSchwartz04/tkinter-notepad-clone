"""
Simple text editor using Python and Tkinter.

Based on a tutorial : https://www.youtube.com/watch?v=xqDonHEYPgA
Modified/extended by Nicholas Schwartz
"""

from tkinter import *
from tkinter.filedialog import *
from tkinter.font import Font
from tkinter.messagebox import *
from tkinter import simpledialog
import os 

filename = None

def newFile():
    global filename
    filename = "Untitled"
    root.title(f"Nick's Text Editor : {filename}")
    text.delete(0.0, END)

def saveFile():
    global filename

    if filename == 'Untitled' or filename == None:  #If the file has not been saved already
        saveFileAs()
    else:
        t = text.get(0.0, END)
        textFile = open(filename, 'w')
        textFile.write(t)
        textFile.close()

def saveFileAs():
    global filename
    file = asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(0.0, END)
    filename = os.path.basename(file.name) #Gets only .txt file name from path
    filename = os.path.splitext(filename)[0]

    try:
        file.write(t.rstrip())
        root.title(f"Nick's Text Editor : {filename}")
    except:
        showerror(title="Error", message="Unable to save file")

def openFile():
    global filename
    f = askopenfile(mode='r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)

    filename = os.path.basename(f.name)
    filename = os.path.splitext(filename)[0]

    root.title(f"Nick's Text Editor : {filename}")

def clearFile():
    text.delete(0.0, END)

def editTextSize():
    size = simpledialog.askinteger("Text Size", "Chose your desired text size")
    user_font.configure(size=size)
    text.pack()


root = Tk()
root.title(f"Nick's Text Editor : Untitled")
root.minsize(width = 200, height = 200)
root.maxsize(width = 500, height = 500)

user_font = Font(family="Arial", size=12)
text = Text(root, width = 200, height = 200, font=user_font)

text.pack()

menuBar = Menu(root)
filemenu = Menu(menuBar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label = "Open", command = openFile)
filemenu.add_command(label = "Save", command = saveFile)
filemenu.add_command(label = "Save As", command = saveFileAs)
filemenu.add_command(label = "Clear Page", command = clearFile)
filemenu.add_command(label = "Change Text Size", command = editTextSize)
filemenu.add_separator()
filemenu.add_command(label = "Quit", command = root.quit)
menuBar.add_cascade(label = "File", menu = filemenu)

root.config(menu = menuBar)
root.mainloop()
