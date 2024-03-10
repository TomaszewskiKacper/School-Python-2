import tkinter as tk
import numpy as np
from numpy import sqrt, exp, pi, log10, log, sin, sinh, cos, cosh, tan, tanh, e

def Submit(text):
    entry1.insert(tk.END, text)

def Add_Button(txt, row, column):
    button = tk.Button(root, text=txt, width=5, height=2, borderwidth=5, command=lambda: Submit(txt))
    button.grid(row=row, column=column, padx=0, pady=0)
    buttons.append(button)

def evaluate():
    txt = entry1.get()
    #modifu text for evaluation
    txt = txt.replace("^", "**")
    txt = txt.replace("log", "log10")
    txt = txt.replace("ln", "log")

    print("attempt to eval: ", txt)
    entry1.delete(0,tk.END) #delete old text

    try:
        entry1.insert(0, eval(txt))   #write new text 
    except Exception as e:
        entry1.insert(0, "ERROR")
        print("error while computing: ", txt, "\nerror: ", e)


def rem():
    txt = entry1.get()
    txt = txt[:-1]  #remove last char
    entry1.delete(0,tk.END) #delete old text
    entry1.insert(0,txt)

def rem_all():
    entry1.delete(0,tk.END) #delete old text


#main window
root = tk.Tk()
root.title("Kalkulator")

#entries
entry1 = tk.Entry(root, width=50)
entry1.grid(row=0, column=0, padx=10, pady=5, columnspan=7)


#buttons
buttons = []

#numbers
Add_Button("1", 1, 0)
Add_Button("2", 1, 1)
Add_Button("3", 1, 2)
Add_Button("4", 2, 0)
Add_Button("5", 2, 1)
Add_Button("6", 2, 2)
Add_Button("7", 3, 0)
Add_Button("8", 3, 1)
Add_Button("9", 3, 2)
Add_Button("<-", 4, 0)#backspace
Add_Button("0", 4, 1)
Add_Button(".", 4, 2)
Add_Button("(", 5, 0)
Add_Button(")", 5, 1)
Add_Button("=", 5, 2)

buttons[9].config(command=rem)#"<-"
buttons[14].config(command=evaluate)#"="

#basic operations
Add_Button("+", 1, 4)
Add_Button("-", 2, 4)
Add_Button("*", 3, 4)
Add_Button("/", 4, 4)
Add_Button("^", 1, 5)
Add_Button("sqrt", 2, 5)
Add_Button("e", 3, 5)
Add_Button("pi", 4, 5)
Add_Button("C", 1, 6)
Add_Button("exp", 2, 6)
Add_Button("log", 3, 6)
Add_Button("ln", 4, 6)

buttons[23].config(command=rem_all)#"C"


#trig operations
Add_Button("sin", 8, 4)
Add_Button("cos", 8, 5)
Add_Button("tan", 8, 6)

Add_Button("sinh", 9, 4)
Add_Button("cosh", 9, 5)
Add_Button("tanh", 9, 6)








#
root.mainloop()