import SzyfrCezara
import datetime
import os

txt = ""    #text to encode


#getting file
while True:
    path = input("Podaj sciezke do pliku: \n")  #sciezka do pliku podana przez uzytkownika

    try:
        with open(path, "r", encoding = "utf-8") as file:   #open file and get contents
            txt = file.read()
        break;  #break out of loop if succes
    except FileNotFoundError:   #Nie znaleziono pliku
        print("Nie znaleziono podanego pliku...")
    except IOError: #Nie mo¿na odczytaæ pliku
        print("Blad odczytu pliku...")
    except Exception as e:  
        print("Error: ", e)


#getting shift
while True:
    try:
        shift = int(input("Podaj przesuniecie [1 - 10]: \n"))

        if not 1 <= shift <= 10:    #zakres [1 - 10]
            raise ValueError("Przesuniecie musi byc liczba calkowita z zakresu [1 - 10]")
        break; #break out of loop if succes
    except ValueError as e:
        print("Wprowadzono zla wartosc przesuniecia. ",e)
    except Exception as e:  
        print("Error: ", e)





#encode
txt = SzyfrCezara.szyfruj(txt, shift)

#save to file
curr_time = datetime.datetime.now()

while True:
    try:
        s_path = input("podaj katalog do zapisania pliku: \n")  #get path from user 
        os.makedirs(os.path.dirname(s_path), exist_ok=True) #create directory if not exist
        s_path += "plik_zaszyfrowany%{}_%{}%{}%{}.txt".format(shift, curr_time.year, curr_time.month, curr_time.day)

        with open(s_path, "w", encoding="utf-8") as s_file:   #save to file
            s_file.write(txt)

        break; #break out of loop if succes
    except FileNotFoundError:
        print("Nie udalo sie stworzyc katalogu")
    except Exception as e:
        print("Error: ", e)



