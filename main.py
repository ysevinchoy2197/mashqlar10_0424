#3-misol
class Kitob:
    def __init__(self, nomi, muallif):
        self.nomi = nomi
        self.muallif = muallif

    def info(self):
        print(self.nomi)


class Darslik(Kitob):
    def info(self):
        print(f"{self.nomi} - Bu darslik")


# 2 obyekt
k1 = Kitob("Alifbe", "Muallif A")
k2 = Darslik("Matematika", "Muallif B")

k1.info()
k2.info()
