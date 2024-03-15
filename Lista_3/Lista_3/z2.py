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

    


u = Ulamek(10,4)
u.wypisz()
u.skroc()
u.wypisz()
 