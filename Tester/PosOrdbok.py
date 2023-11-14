# list = [row1, row2, row3, col1, col2, col3, diag1, diag2]
# Vi kan med denne subtrahere hvis spiller 2 berører og addere hvis spiller 1 gjør trekk der.
# Etter hver kan vi deaktivere resten av listen så vi ikke sparer på mer data enn nødvendig

# posisjon = []

# for i in range(1,10):
#     cond = "long"
#     if i < 4: 
#         posisjon.append("x")
#     else:
#         posisjon.append(".")

#     if i == 2 or i == 4 or i == 6 or i == 8:
#         cond = "short"
#     else:
#         cond = "long"
    

# print(posisjon)

class TTT:
    def __init__(self) -> None:
        self.Spiller1avat = "X"
        self.Spiller1Scr = 1

        self.Spiller2avat = "O"
        self.Spiller2Scr = -1

        self.RuteTom = ""
        self.game = True

    def gen_game(self, strls:int):
        self.rutenett = []
        for i in range(1, strls + 1): 
            self.rutenett.append(self.RuteTom)

    def draw(self):
        for brikke in self.rutenett:
            pass



spill = TTT()
spill.gen_game(9)
print(spill.rutenett)

while spill.game == True:
    pass