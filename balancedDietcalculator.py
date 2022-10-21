#Balanced Diet Calcuiator
import tkinter as tk
from tkinter import *
import BMIcalculator as bmi

win = tk.Tk()
win.title("Balanced Diet Calculator")
win.geometry("350x125")

def calc():
    p1 = float(entry1.get())
    protein = p1 * 1.2
    fat = p1 * 0.75
    carbs = p1 * 2
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)
    entry2.insert(0, protein)
    entry3.insert(0, fat)
    entry4.insert(0, carbs)

entry1 = tk.Entry(win, width = 25)
entry2 = tk.Entry(win, width = 25, background="#c7bea5")
entry3 = tk.Entry(win, width = 25, background="#c7bea5")
entry4 = tk.Entry(win, width = 25, background="#c7bea5")
l1 = tk.Label(win,text="Enter your weight in kg : ")
l2 = tk.Label(win,text="Protein : ")
l3 = tk.Label(win,text="Carbohydrates : ")
l4 = tk.Label(win,text="Fats : ")
b1 = tk.Button(win,text="Calculate",activebackground="orange", activeforeground="white",command=calc)
l_grams1 = tk.Label(win,text="grams")
l_grams2 = tk.Label(win,text="grams")
l_grams3 = tk.Label(win,text="grams")
l_kg = tk.Label(win,text="kg")

menu = Menu(win)
win.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='Apps', menu=filemenu)
filemenu.add_command(label='BMI', command=bmi.BMI)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=win.quit)

l1.grid(row=1,column=0,sticky="W")
l2.grid(row=2,column=0,sticky="W")
l3.grid(row=3,column=0,sticky="W")
l4.grid(row=4,column=0,sticky="W")
l_kg.grid(row=1,column=2,sticky="W")
l_grams1.grid(row=2,column=2,sticky="W")
l_grams2.grid(row=3,column=2,sticky="W")
l_grams3.grid(row=4,column=2,sticky="W")
entry1.grid(row=1,column=1)
entry2.grid(row=2,column=1)
entry3.grid(row=3,column=1)
entry4.grid(row=4,column=1)
b1.grid(row=5,column=1)

win.mainloop()

