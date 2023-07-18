import pygame
from scripts.utils.Obj import Obj
from scripts.utils.constants import *

class Tiro(Obj):
    def __init__(self, pos, *groups):
        super().__init__("assets/tiros/tiro3.png", pos, *groups)
        self.velocidade = 7
        self.dano = 1
        self.tempo = 10
        self.som = pygame.mixer.Sound("assets/Sounds/shot.ogg")
        self.som.play()

    def update(self):
        self.rect.y -= self.velocidade
        if self.rect.y <= -100:
            self.kill()