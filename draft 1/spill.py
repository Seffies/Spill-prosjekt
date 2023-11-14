import pygame as pg


pg.init()
BREDDE = 600
HOYDE = 600
FPS = 60
vindu = pg.display.set_mode((BREDDE,HOYDE))
klokke = pg.time.Clock()
Constx = 100
Consty = 100
spill = []
aktiveRuter = []
tur = 1 

class TicTacToeBox():
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y
        self.farge = "white"
        self.okkupasjon = False
        pass
    
    def draw(self, vindu):
        pg.draw.circle(vindu, self.farge, [self.x, self.y], 10)
    
    def sjekkPos(self, mus_x, mus_y, tur):
        if self.x - 10 < mus_x < self.x +10 and self.y - 10 < mus_y < self.y + 10:
            if self.okkupasjon == False:
                self.okkupasjon = True
                if tur == 1:
                    self.farge = "blue"
                if tur == 2: 
                    self.farge = "red"


lengde = 3


for i in range(0,lengde):
    for j in range(0,lengde):
        spill.append(TicTacToeBox(Constx + j*30, Consty + i *30))


for i in range(len(spill)):
    aktiveRuter.append(i)

while True:
    for hendelse in pg.event.get():
        if hendelse.type == pg.QUIT:
            pg.quit()
            raise SystemExit
        
        mus_x, mus_y = pg.mouse.get_pos()

        for i in range(len(spill)):
            spill[i].sjekkPos(mus_x, mus_y, tur)
            if spill[i].okkupasjon == True and tur == 1 and i in aktiveRuter:
                tur = 2
                aktiveRuter.remove(i)
            elif spill[i].okkupasjon == True and i in aktiveRuter: 
                tur = 1
                aktiveRuter.remove(i)
            spill[i].draw(vindu)


        pg.display.flip()
        klokke.tick(FPS)