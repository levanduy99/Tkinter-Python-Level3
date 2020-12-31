import tkinter
from tkinter import*
from tkinter import messagebox
import random

# you can add more words as per your requirement
answers = [
    "python",
    "java",
    "vietnam",
    "canada",
    "india",
    "america",
    "london",
]

words = [
    "nptoyh",
    "avja",
    "manteiv",
    "cdanaa",
    "aidin",
    "aiearcm",
    "odnlon",
]

num = random.randrange(0,len(words),1)

def default():
    global words,answers,num
    lbl.config(text = words[num])

def res():
    global words,answers,num
    num = random.randrange(0,len(words),1)
    lbl.config(text = words[num])
    e1.delete(0,END)

def checkans():
    global words,answers,num
    var = e1.get()
    if var == answers[num]:
        messagebox.showinfo("Success", "This is a correct answer")
        res()
    else:
        messagebox.showerror("Error", "This is not Correct")
        e1.delete(0, END)

root = tkinter.Tk()
root.geometry("350x400+400+300")
root.title("Check Word")
root.configure(background = "#000000")

lbl = Label(
    root,
    text = "Your here",
    font = ("Verdana", 18),
    bg = "#000000",
    fg = "#FFFFFF",
)
lbl.pack(pady = 30,ipady=10,ipadx=10)

e1 = Entry(
    root,
    font = ("Verdana", 16),
    textvariable = StringVar(),

)
e1.pack(ipady=5,ipadx=5)

btncheck = Button(
    root,
    text = "Check",
    font = ("Comic sans ms", 16),
    width = 16,
    bg = "#4c4b4b",
    fg = "#6ab04c",
    command = checkans,

)
btncheck.pack(pady = 40)

btnreset = Button(
    root,
    text = "Reset",
    font = ("Comic sans ms", 16),
    width = 16,
    bg = "#4c4b4b",
    fg = "#EA425C",
    command = res,

)
btnreset.pack()
default()
root.mainloop()
