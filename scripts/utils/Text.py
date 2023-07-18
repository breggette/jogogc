import pygame
from scripts.utils.constants import *

class Text():
    def __init__(self, texto, cor, tamanho):
        self.display = pygame.display.get_surface()

        self.font = pygame.font.Font("assets/fonts/airstrike.ttf", tamanho)
        self.font_rend = self.font.render(texto, True, cor)

    def drawCenter(self):
        self.font_rect = self.font_rend.get_rect(center=[TELA_LARGURA / 2, TELA_ALTURA / 2])
        self.display.blit(self.font_rend, self.font_rect)

    def draw(self,pos=[0,0]):
        self.font_rect = self.font_rend.get_rect(topleft=pos)
        self.display.blit(self.font_rend, self.font_rect)
