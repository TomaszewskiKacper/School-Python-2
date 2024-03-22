import math

class Ulamek:
    def __init__(self, numerator, denominator): #constructor
        self.a = numerator      #assuming fraction in form [a/b]
        self.b = denominator

    def __new__(cls, numerator, denominator):   #new nic nie robi w tym przypadku
        if isinstance(numerator, int) and isinstance(denominator, int):
            return object.__new__(cls)
        else:
            print("numerator i denominator musza byc liczbami calkowitymi")
            return None

    def wypisz(self):
        print(self.a, "/", self.b)

    def skroc(self):
        div = math.gcd(self.a, self.b)
        self.a //= div
        self.b //= div

    @staticmethod
    def dodaj(x, y):
        a = (x.a * y.b) + (y.a * x.b)
        b = x.b * y.b
        return Ulamek(a,b)

    @staticmethod
    def odejmij(x, y):
        a = (x.a * y.b) - (y.a * x.b)
        b = x.b * y.b
        return Ulamek(a,b)

    @staticmethod
    def mnoz(x, y):
        a = x.a * y.a
        b = x.b * y.b
        return Ulamek(a,b)

    @staticmethod
    def dziel(x, y):
        a = x.a * y.b
        b = x.b * y.a
        return Ulamek(a,b)


    


u1 = Ulamek(10,4)
u2 = Ulamek(5,3)


#testowanie
u1.wypisz()
u1.skroc()
print("skrocone: ")
u1.wypisz()
print("")
u1.wypisz()
u2.wypisz()
print("dodane: ")
u3 = Ulamek.dodaj(u1, u2)
u3.wypisz()
print("odejmowane: ")
u3 = Ulamek.odejmij(u1,u2)
u3.wypisz()
print("mnozone: ")
u3 = Ulamek.mnoz(u1,u2)
u3.wypisz()
print("dzielone: ")
u3 = Ulamek.dziel(u1,u2)
u3.wypisz()


 