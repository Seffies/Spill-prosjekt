import pygame as pg

pg.init()
BREDDE = 360
HOYDE = 360
FPS = 60
vindu = pg.display.set_mode((BREDDE,HOYDE))
klokke = pg.time.Clock()
constx = 25
consty = 25
tur = 1
klick = False
lengde = 3
aktivind = None


pg.display.set_caption("Ultimate Tic Tac Toe")


class Rutenett():
    def __init__(self, ruter, x:int, y:int) -> None:
        self.bredde = 120
        self.hoyde = 120
        self.nett = []
        for i in range(0,lengde):
            for j in range(0,lengde):
                self.nett.append(ruter(x + j*35, y + i *35))

    def sjekkVinn():
        pass

        


class TTT():
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y
        self.radius = 15
        self.state = 0

        self.spiller1farg = (0, 0, 204)
        self.spiller1score = 1

        self.spiller2farg = (204, 0, 0)
        self.spiller2score = -1

        self.aktiv = False
        self.aktivfarg = "white"
        self.inaktivfarg = "white"

    def draw(self, vindu:pg.Surface):
        pg.draw.circle(vindu, "black", [self.x, self.y], self.radius)
        if aktivind == None or self.aktiv == True:
            pg.draw.circle(vindu, self.aktivfarg, [self.x, self.y], self.radius - 2)
        else:
            pg.draw.circle(vindu, self.inaktivfarg, [self.x, self.y], self.radius - 2)
    
    def sjekkPos(self, mus_x, mus_y, tur):
        if self.x - self.radius < mus_x < self.x + self.radius and self.y - self.radius < mus_y < self.y + self.radius:
            if self.state == 0:
                if tur == 1:
                    self.aktivfarg = self.spiller1farg
                    self.state += self.spiller1score 
                if tur == 2: 
                    self.aktivfarg = self.spiller2farg
                    self.state += self.spiller2score 
                print("denne stemmer")
            return True

        else:
            return False
                    


storspill = []
for i in range(0,lengde):
    for j in range(0,lengde):
        storspill.append(Rutenett(TTT, constx + j*120, consty + i*120))

print(storspill)


while True:

    for hendelse in pg.event.get():
        if hendelse.type == pg.QUIT:
            pg.quit()
            raise SystemExit
        if hendelse.type == pg.MOUSEBUTTONDOWN:
            mus_x, mus_y = pg.mouse.get_pos()
            for i in range(len(storspill)):
                for j in range(len(storspill[i].nett)):
                    storspill[i].nett[j].sjekkPos(mus_x, mus_y, tur)
                    print(storspill[i].nett[j].sjekkPos(mus_x, mus_y, tur))
                    if storspill[i].nett[j].sjekkPos(mus_x, mus_y, tur) == True:
                        aktivind = j
                        print("denne fikk index", aktivind)

            if tur == 1 and klick == False:
                tur = 2
                klick = True
            elif klick == False:
                klick = True
                tur = 1
        if hendelse.type == pg.MOUSEBUTTONUP:
            klick = False
                
    if tur == 1: 
        vindu.fill((102,178,255))
    elif tur == 2: 
        vindu.fill((255,102,102))

    for i in range(len(storspill)):
        for j in range(len(storspill[i].nett)):
            storspill[i].nett[j].draw(vindu)
    pg.display.flip()
    klokke.tick(FPS)