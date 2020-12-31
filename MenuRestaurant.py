import tkinter
from tkinter import*

window = Tk()
window.geometry("700x500")

def calculate():
    cap = e1.get()
    if(cap == ""):
        cap = 0
    esp = e2.get()
    if(esp == ""):
        esp = 0
    tea = e3.get()
    if(tea == ""):
        tea = 0
    cho = e4.get()
    if(cho == ""):
        cho = 0
    total= int(cap)*5 + int(esp)*2 + int(tea)*3 + int(cho)*4
    label12 = Label(window,text=total,font="times 18")
    label12.place(x=100,y=360)
#----menu section-----

label6 = Label(window,text="PHUC LONG",font="times 30 bold",fg="#29B966")
label6.place(x=350,y=20,anchor="center")

label1 = Label(window,text="MENU",font="times 28 bold")
label1.place(x=500,y=70)

label2 = Label(window,text="Cappuccino     5$",font="times 18")
label2.place(x=450,y=120)

label3 = Label(window,text="Espresso          2$",font="times 18")
label3.place(x=450,y=150)

label4 = Label(window,text="Tea                  3$",font="times 18")
label4.place(x=450,y=180)

label5 = Label(window,text="Chocolate        4$",font="times 18")
label5.place(x=450,y=210)
#------billing section---------
label7 = Label(window,text="Select the items",font="times 20 bold")
label7.place(x=70,y=70)

label8 = Label(window,text="Cappuccino",font="times 18")
label8.place(x=20,y=120)

e1 = Entry(window)
e1.place(x=20,y=150)

label9 = Label(window,text="Espresso",font="times 18")
label9.place(x=250,y=120)

e2 = Entry(window)
e2.place(x=250,y=150)

label10 = Label(window,text="Chocolate",font="times 18")
label10.place(x=20,y=180)

e3 = Entry(window)
e3.place(x=20,y=210)

label11 = Label(window,text="Tea",font="times 18")
label11.place(x=250,y=180)

e4 = Entry(window)
e4.place(x=250,y=210)

b1 = Button(window,text="BILL",width="20",fg="#FF3031",font="times 18 bold",command=calculate)
b1.place(x=100,y=300)


window.mainloop()
