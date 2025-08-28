from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
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
    text = Text(root, width = 400, height = 400)
    text.pack()

root = Tk()
root.title(f"Nick's Text Editor : Untitled")
root.minsize(width = 200, height = 200)
root.maxsize(width = 500, height = 500)

text = Text(root, width = 200, height = 200)
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

