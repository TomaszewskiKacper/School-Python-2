# Szyfr Cezara

#Funkcja szyfruj¹ca
def szyfruj(text, shift):
    result = ""
    for el in text:     #loop through each character
        if el.isalpha():    #only letters
            if el.lower() in ["\u0105", "\u0107", "\u0119", "\u0142", "\u0144", "\u00f3", "\u015b", "\u017a", "\u017c"]:    #ignore polish letters
                result += el
                continue


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
