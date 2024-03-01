# Szyfr Cezara

#Funkcja szyfruj¹ca
def szyfruj(text, shift):
    result = ""
    for el in text:     #loop through each character
        if el.isalpha():    #only letters

            szyfrowane = ord(el) + shift

            if el.islower():    #lower case
                if szyfrowane > ord("z"):
                    szyfrowane -= 26
                elif szyfrowane< ord("a"):
                    szyfrowane += 26

            elif el.isupper():  #upper case
                if szyfrowane > ord("Z"):
                    szyfrowane -= 26
                elif szyfrowane< ord("A"):
                    szyfrowane += 26

            result += chr(szyfrowane)    #add to result
        else:
            result += el
        
    return result
      







def deszyfruj(text, shift):
    return szyfruj(text, -shift)
