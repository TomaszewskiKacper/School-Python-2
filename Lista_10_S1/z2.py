import SzyfrCezara
import datetime
import os

while True: #get directory path from user
    try:
        path = input("Podaj sciezke do katalogu: \n")   #input from user
        files = os.listdir(path)    #list of all files in directory
        break
    except FileNotFoundError:
        print("Nie znaleziono katalogu...")
    except Exception as e:
        print("error: ",e)

while True: #get directory path from user
    try:
        s_path = input("Podaj sciezke do katalogu gdzie zapisac odszyfrowane: \n")   #input from user
        os.makedirs(os.path.dirname(s_path), exist_ok=True) #create directory if not exist
        break
    except FileNotFoundError:
        print("Nie znaleziono katalogu...")
    except FileNotFoundError:
        print("Nie udalo sie stworzyc katalogu")
    except Exception as e:
        print("error: ",e)


for file in files:  #go through all the files
    if file.startswith("plik_zaszyfrowany"):    #encoded file...
        v = file.split("%") #extract variables
        v = v[1:]

        f_path = path + file    #file path
        with open(f_path, "r", encoding="utf-8") as f:    #open encoded file
            txt = f.read()  #read file

        shift = int("".join(filter(str.isdigit, v[0]))) #get shift from extracted variables
        txt = SzyfrCezara.deszyfruj(txt, shift)    #decode text
        
        d_path = "" #new path 
        d_path += s_path
        d_path += "plik_deszyfrowany%{}_%{}%{}%{}.txt".format(v[0], v[1], v[2], v[3])

        with open(d_path, "w", encoding="utf-8") as f:
            f.write(txt)
