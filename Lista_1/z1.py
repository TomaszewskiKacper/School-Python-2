import tkinter as tk

def Submit():
    print("Imie i Nazwisko: ", entry1.get())
    print("Numer Indeksu: ", entry2.get())
    print("Haslo: ", entry1.get())
    return True

def Button_check():
    if entry1.get() and entry2.get() and entry3.get():
        button.config(state=tk.NORMAL, text="Przeslij", borderwidth=3)
    else:
        button.config(state=tk.DISABLED, text="", borderwidth=0)

def Number_check(n_value):
    if n_value.isdigit() or n_value == "":
        return True
    else:
        return False



#main window
root = tk.Tk()
root.title("Formularz")

#entries
label1 = tk.Label(root, text="Imie i Nazwisko")
label1.grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=5)
entry1.bind("<KeyRelease>", lambda event: Button_check())

label2 = tk.Label(root, text="Numer Indeksu")
label2.grid(row=1, column=0, padx=10, pady=5)
check_num = root.register(Number_check)
entry2 = tk.Entry(root, validate="key", validatecommand=(check_num, "%P"))
entry2.grid(row=1, column=1, padx=10, pady=5)
entry2.bind("<KeyRelease>", lambda event: Button_check())


label3 = tk.Label(root, text="Haslo")
label3.grid(row=2, column=0, padx=10, pady=5)
entry3 = tk.Entry(root, show="*")
entry3.grid(row=2, column=1, padx=10, pady=5)
entry3.bind("<KeyRelease>", lambda event: Button_check())


#button
button = tk.Button(root, text="", command=Submit, state=tk.DISABLED, borderwidth=0)
button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)




#
root.mainloop()