import SzyfrCezara


txt = "tekst do zAAAAaszyfrowania\ntest"
print(txt)
txt = SzyfrCezara.szyfruj(txt, 10)
print(txt)
txt = SzyfrCezara.deszyfruj(txt, 10)
print(txt)
