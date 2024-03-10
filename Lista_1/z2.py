import tkinter as tk
import SzyfrCezara

def Submit():
    txt = SzyfrCezara.szyfruj(entry1.get(), int(entry2.get()))  #tekst zaszyfrowany
    entry3.config(state=tk.NORMAL)  #enable to change text
    entry3.delete(0,tk.END) #delete old text
    entry3.insert(0, txt)   #write new text 
    entry3.config(state=tk.DISABLED)    #disable

def Button_check():
    if entry1.get() and entry2.get():
        button.config(state=tk.NORMAL)
    else:
        button.config(state=tk.DISABLED)

def Number_check(n_value):
    if n_value.isdigit() or n_value == "":
        return True
    else:
        return False



#main window
root = tk.Tk()
root.title("Formularz")

#entries
label1 = tk.Label(root, text="Tekst do zaszyfrowania: ")
label1.grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=5)
entry1.bind("<KeyRelease>", lambda event: Button_check())

label2 = tk.Label(root, text="Przesuniecie: ")
label2.grid(row=1, column=0, padx=10, pady=5)
check_num = root.register(Number_check)
entry2 = tk.Entry(root, validate="key", validatecommand=(check_num, "%P"))
entry2.grid(row=1, column=1, padx=10, pady=5)
entry2.bind("<KeyRelease>", lambda event: Button_check())


label3 = tk.Label(root, text="Zakodowany tekst: ")
label3.grid(row=2, column=0, padx=10, pady=5)
entry3 = tk.Entry(root, state=tk.DISABLED)
entry3.grid(row=2, column=1, padx=10, pady=5)



#button
button = tk.Button(root, text="Szyfroj", command=Submit, state=tk.DISABLED)
button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)




#
root.mainloop()