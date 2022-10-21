#BMI Calculator
import tkinter as tk
from tkinter import *

def BMI():
    win = tk.Tk()
    win.title("BMI Calculator")
    win.geometry("350x125")

    def calc():
        weight = float(entry1.get())
        height = float(entry2.get()) / 100
        bmi = weight / (height * height)
        entry3.delete(0, tk.END)
        entry3.insert(0, bmi)
        if bmi < 18.5:
            lbl_result.config(text="You are Underweight")
        elif bmi >= 18.5 and bmi < 25:
            lbl_result.config(text="You are Normal")
        elif bmi >= 25 and bmi < 30:
            lbl_result.config(text="You are Overweight")
        elif bmi >= 30:
            lbl_result.config(text="you are Obese")
        
    lbl_head = tk.Label(win,text="Enter Weight in kg : ")
    lbl_head2 = tk.Label(win,text="Enter Height in cm : ")
    lbl_result = tk.Label(win,text="")
    entry1 = tk.Entry(win, width = 25)
    entry2 = tk.Entry(win, width = 25)
    entry3 = tk.Entry(win, width = 25)

    button1 = tk.Button(win,text="Calculate",command=calc)

    lbl_head.grid(row=0,column=0,sticky="W")
    lbl_head2.grid(row=1,column=0,sticky="W")
    entry1.grid(row=0,column=1)
    entry2.grid(row=1,column=1)
    entry3.grid(row=2,column=1)
    button1.grid(row=2,column=0)
    lbl_result.grid(row=3,column=1)

    win.mainloop()