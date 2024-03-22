class Student:
    def __init__(self, Imie, Nazwisko, Index): #constructor
        self.imie = Imie      
        self.nazwisko = Nazwisko
        self.index = Index
        self.przedmioty = dict()
        self.ocena = 0

    def Update(self):
        if len(self.przedmioty) != 0:
            o = 0
            for p in self.przedmioty:
                o+= self.przedmioty[p]
            o /= len(self.przedmioty)
            self.ocena = o     
        else:
            self.ocena = 0

       

    def Dodaj_przedmiot(self, przedmiot, ocena):
        self.przedmioty[przedmiot] = ocena
        self.Update()

    def Usun_przedmiot(self, przedmiot):
        del self.przedmioty[przedmiot]
        self.Update()


s = Student("Kac", "Tom", 33)
s.Dodaj_przedmiot("a", 5)
s.Dodaj_przedmiot("b", 4)
s.Dodaj_przedmiot("c", 3)
s.Dodaj_przedmiot("d", 2)
print(s.ocena)
s.Usun_przedmiot("a")
s.Usun_przedmiot("b")
s.Usun_przedmiot("c")
s.Usun_przedmiot("d")
print(s.ocena)
    

    





