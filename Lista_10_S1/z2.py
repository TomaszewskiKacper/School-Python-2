import SzyfrCezara
import datetime
import os

while True: #get directory path from user
    try:
        path = input("Podaj sciezke do katalogu: \n")   #input from user
        files = os.listdir(path)    #list of all files in directory

        for file in files:
            if file.startswith("plik_zaszyfrowany"):    #encoded file...
                v = file.split("%") #extract variables
                v = v[1:]

                f_path = path + file    #file path
                with open(f_path, "r") as f:    #open encoded file
                    txt = f.read()  #read file

                shift = int("".join(filter(str.isdigit, v[0]))) #get shift from extracted variables
                txt = SzyfrCezara.deszyfruj(txt, -shift)    #decode text




        





    except :
        pass