import pygame
from scripts.utils.constants import *

class BgAnimado():
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.bg = pygame.image.load("assets/menu/galax.png")
        self.bg2 = pygame.image.load("assets/menu/galax.png")

        self.bg = pygame.transform.scale(self.bg, (TELA_LARGURA, TELA_ALTURA))
        self.bg2 = pygame.transform.scale(self.bg2, (TELA_LARGURA, TELA_ALTURA))

        self.bg_rect = self.bg.get_rect()
        self.bg2_rect = self.bg2.get_rect(top=-TELA_ALTURA)

        self.velocidade = 1

    def update(self):
        self.bg_rect.y += self.velocidade
        self.bg2_rect.y += self.velocidade

        if self.bg_rect.y >= TELA_ALTURA:
            self.bg_rect.y = -TELA_ALTURA

        if self.bg2_rect.y >= TELA_ALTURA:
            self.bg2_rect.y = -TELA_ALTURA

    def draw(self):
        self.update()
        self.display.blit(self.bg, self.bg_rect)
        self.display.blit(self.bg2, self.bg2_rect)