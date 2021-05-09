import os
from tkinter import *

def submit():
    inp3 = box3.get(1.0, "end-1c")
    if (inp3) == "addition":
        inp = box1.get(1.0, "end-1c")
        inp2 = box2.get(1.0, "end-1c")
        su = float(inp) + float(inp2)
        box4 = Label(root, text = (su))
        box4.pack()
    if (inp3) == "subtraction":
        inp = box1.get(1.0, "end-1c")
        inp2 = box2.get(1.0, "end-1c")
        su = float(inp) - float(inp2)
        box4 = Label(root, text = (su))
        box4.pack()
    if (inp3) == "multiplication":
        inp = box1.get(1.0, "end-1c")
        inp2 = box2.get(1.0, "end-1c")
        su = float(inp) * float(inp2)
        box4 = Label(root, text = (su))
        box4.pack()
    if (inp3) == "division":
        inp = box1.get(1.0, "end-1c")
        inp2 = box2.get(1.0, "end-1c")
        su = float(inp) / float(inp2)
        box4 = Label(root, text = (su))
        box4.pack()
    if (inp3) != "division" or "addition" or "subtraction" or "multiplication":
        box4 = Label(root, text = "Values: addition, subtraction, \ndivision, or multiplication in the bottom box")
        box4.pack()

valv = "PY-CAL"
root=Tk()
root.title("PY-CAL by Nesanco")
txt1=Label(root,height="5",width="250",bg='brown',fg='white', text = (valv),font=('Helvetica','25','bold'))
box1=Text(root, height=3, width=20)
box2=Text(root, height=3, width=20)
box3=Text(root, height=3, width=20)
btn1=Button(root, height=3, width=10, fg='white', bg='olive', text="Submit", command=submit)
root.configure(bg='brown')
root.geometry('400x700')
print("Startup")
txt1.pack()
box1.pack()
box2.pack()
btn1.pack()
box3.pack()
mainloop()
