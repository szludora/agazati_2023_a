class Gomba:
    def __init__(self, nev, nemzettseg, evszak):
        self.nev = nev
        self.nemzettseg = nemzettseg
        self.evszak = evszak

    def __str__(self):
        return f"{self.nev}, {self.nemzettseg}, {self.evszak}"
