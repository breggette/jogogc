import pygame
import random
from scripts.utils.constants import *
from scripts.utils.Obj import Obj
from scripts.elements.Explosao import Explosao

class Inimigo(Obj):
    def __init__(self, *groups):
        posx = random.randint(100, TELA_LARGURA - 100)
        posy = -100
        super().__init__("assets/nave/enemy0.png", (posx, posy), *groups)

        self.vida = 1
        self.velocidade = random.randint(3, 10)

    def dano(self, grupo):
        self.vida -= 1
        if self.vida <= 0:
            Explosao((self.rect.x, self.rect.y), [grupo])
            self.kill()


    def update(self, *args):
        self.rect.y += self.velocidade
        if self.rect.y > TELA_ALTURA + 100:
            self.kill()

        self.animate(5, [
            "assets/nave/enemy0.png",
            "assets/nave/enemy1.png",
            "assets/nave/enemy2.png"
        ])
