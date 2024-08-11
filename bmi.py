from future.moves import tkinter
from tkinter import ttk
from tkinter import *

def bmi():
    height = float(h.get())
    Weight = float(w.get())
    BMI = round(float(Weight / height** 2), 1) 
    label.config(text=BMI)  

    # conditions
    if BMI <= 18.5:
        label1.config(text="You are Underweight")
    elif BMI > 18.5 and BMI <= 25:
        label1.config(text="You are Normal")
    elif BMI > 25 and BMI <= 30:
        label1.config(text="You are Overweight")
    else:
        label1.config(text="Health is at risk!")

master = tkinter.Tk()
master.title("BMI calculator")
master.geometry("500x600+300+200")

top = tkinter.Label (master, text="BMI CALCULATOR", font=("Verdana", 25, "bold"), width=25, bd=5, bg="lightcyan")
top.place(x=0, y=0)
tkinter.Label (master, width=70, height=25, bg="lightgrey").pack(side="bottom")

h_box = tkinter.DoubleVar()
def height_box():
    return '{: .2f}'.format(h_box.get())
style_h = ttk.Style()
style_h.configure("TScale", background="white")

w_box = tkinter.DoubleVar()
def weight_box():
    return '{: .2f}'.format(h_box.get())

height = tkinter.StringVar()
weight = tkinter.StringVar()
h = tkinter.Entry (master, textvariable=height, width=5, font=("Verdana", 50), bg="white", fg="black", bd=0,
                  justify="center")
h.place(x=35, y=160)
hei=tkinter.Label(master, text="Height in mtr:", font=("Verdana", 10, "bold"), width=25, bd=5, bg="lightgrey")
hei.place(x=20, y=125)
height.set(height_box())

w = tkinter.Entry (master, textvariable=weight, width=5, font=("Verdana", 50), bg="white", fg="black", bd=0,
                  justify="center")
w.place(x=255, y=160)
wei=tkinter.Label(master, text="Weight in kgs:", font=("Verdana", 10, "bold"), width=25, bd=5, bg="lightgrey")
wei.place(x=260, y=125)
weight.set(weight_box())

tkinter.Button (master, text="OK", width=15, height=2, font=("Verdana", 10, "bold"), bg="black", fg="white",
               command=bmi).place(x=180, y=300)

label = tkinter.Label (master, font=("verdana", 30, "bold"), bg="lightgrey", fg="black")
label.place(x=200, y=380)

label1 = tkinter.Label(master, font=("Verdana", 20, "bold"), bg="lightgrey", fg="black")
label1.place(x=150, y=430) 

mainloop()