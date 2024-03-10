import numpy as np

class Kolo:
    def __init__(self, r):
        self.r = r

    def pole(self):
        return np.pi * self.r * self.r

    def obwod(self):
        return np.pi * 2 * self.r


k = Kolo(5)
print("Obwod: ", k.obwod())
print("Pole: ", k.pole())