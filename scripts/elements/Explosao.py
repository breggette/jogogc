import pygame
from scripts.utils.Obj import Obj

class Explosao(Obj):
    def __init__(self, pos, *groups):
        super().__init__("assets/explosion/0.png", pos, *groups)
        self.tempo = 0
        self.som = pygame.mixer.Sound("assets/Sounds/block.ogg")
        self.som.play()

    def update(self):
        self.animate(5,[
            "assets/explosion/0.png",
            "assets/explosion/1.png",
            "assets/explosion/2.png",
            "assets/explosion/3.png",
            "assets/explosion/4.png"
        ])
        self.tempo += 1
        if self.tempo >= 26:
            self.kill()
