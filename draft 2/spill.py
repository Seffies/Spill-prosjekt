import pygame as pg

pg.init()
BREDDE = 600
HOYDE = 600
FPS = 60
vindu = pg.display.set_mode((BREDDE,HOYDE))
klokke = pg.time.Clock()
constx = 100
consty = 100
spill = []
tur = 1

class TTT():
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y

        self.state = 0

        self.spiller1avat = "X"
        self.spiller1farg = "blue"
        self.spiller1score = 1

        self.spiller2avat = "O"
        self.spiller2farg = "red"
        self.spiller2score = -1

        self.spiller0avat = ""
        self.spiller0farg = "white"

    def draw(self, vindu):
        pg.draw.circle(vindu, self.spiller0farg, [self.x, self.y], 12)
    
    def sjekkPos(self, mus_x, mus_y, tur):
        if self.x - 12 < mus_x < self.x +12 and self.y - 12 < mus_y < self.y + 12:
            if self.state == 0:
                if tur == 1:
                    self.spiller0farg = self.spiller1farg
                    self.state += self.spiller1score 
                if tur == 2: 
                    self.spiller0farg = self.spiller2farg
                    self.state += self.spiller2score 
                    

lengde = 3


for i in range(0,lengde):
    for j in range(0,lengde):
        spill.append(TTT(constx + j*30, consty + i *30))




while True:
    for hendelse in pg.event.get():
        if hendelse.type == pg.QUIT:
            pg.quit()
            raise SystemExit
        
        mus_x, mus_y = pg.mouse.get_pos()

        for i in range(len(spill)):
            spill[i].sjekkPos(mus_x, mus_y, tur)

            spill[i].draw(vindu)




        pg.display.flip()
        klokke.tick(FPS)