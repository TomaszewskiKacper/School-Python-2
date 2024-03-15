class Egzamin:
    def __init__(self): #constructor
        self.oceny = dict()

    def __new__(cls):   #new nic nie robi w tym przypadku
      return object.__new__(cls)

    def dodaj(self, student, grade):    #add student and grade
        self.oceny[student] = grade

    def usun(self, student):    #remove student
        del self.oceny[student]

    def show(self): #show sorted dictionary
        sorted_dict = dict(sorted(self.oceny.items(), key= lambda item: item[1]))
        print(sorted_dict)


e = Egzamin()
e.dodaj("Kacper", 2)
e.show()
e.dodaj("Maciej", 4)
e.dodaj("Andrzej", 5)
e.show()
e.usun("Kacper")
e.show()



