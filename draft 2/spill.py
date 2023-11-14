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
klick = False

class TTT():
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y
        self.radius = 60
        self.state = 0

        self.spiller1avat = "X"
        self.spiller1farg = "blue"
        self.spiller1score = 1

        self.spiller2avat = "O"
        self.spiller2farg = "red"
        self.spiller2score = -1

        self.spiller0avat = ""
        self.spiller0farg = "white"

    def draw(self, vindu:pg.Surface):
        pg.draw.circle(vindu, self.spiller0farg, [self.x, self.y], self.radius)
    
    def sjekkPos(self, mus_x, mus_y, tur):
        if self.x - self.radius < mus_x < self.x + self.radius and self.y - self.radius < mus_y < self.y + self.radius:
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
        spill.append(TTT(constx + j*130, consty + i *130))



jo = 0
while True:
    for hendelse in pg.event.get():
        if hendelse.type == pg.QUIT:
            pg.quit()
            raise SystemExit
        if hendelse.type == pg.MOUSEBUTTONDOWN:
            jo += 1
            print("nå", jo)
            mus_x, mus_y = pg.mouse.get_pos()
            for i in range(len(spill)):
                spill[i].sjekkPos(mus_x, mus_y, tur)

            if tur == 1 and klick == False:
                tur = 2
                klick = True
            elif klick == False:
                klick = True
                tur = 1
        if hendelse.type == pg.MOUSEBUTTONUP:
            klick = False

    for i in range(len(spill)):
        spill[i].draw(vindu)
                    
        pg.display.flip()
        klokke.tick(FPS)