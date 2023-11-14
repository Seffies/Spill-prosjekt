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
