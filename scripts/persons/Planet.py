import pygame
import random
from scripts.utils.constants import *
from scripts.utils.Obj import Obj
from scripts.elements.Explosao import Explosao

class Planet(Obj):
    def __init__(self, *groups):
        posx = random.randint(100, TELA_LARGURA - 100)
        posy = -100
        super().__init__("assets/planetas/blue/0.png", (posx, posy), *groups)

        self.velocidade = random.randint(3, 10)

    def update(self, *args):
        self.rect.y += self.velocidade
        if self.rect.y > TELA_ALTURA + 100:
            self.kill()

        self.animate(5, [
            "assets/planetas/blue/0.png",
            "assets/planetas/blue/1.png",
            "assets/planetas/blue/2.png",
            "assets/planetas/blue/3.png",
            "assets/planetas/blue/4.png"
        ])
