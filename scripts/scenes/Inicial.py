import pygame
from scripts.utils.constants import *
from scripts.utils.Text import Text
from scripts.scenes.Jogo import Jogo

class Inicial():
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.scene = self

        self.titulo = Text("SPACE SHIP", BRANCO, 40)
        self.descricao = Text("Pressione qualquer tecla para iniciar", BRANCO, 25)

    def update(self):
        pass

    def draw(self):
        self.titulo.drawCenter()
        self.descricao.draw([
            (TELA_LARGURA / 2) - 280,
            (TELA_ALTURA / 2) + 30
        ])

    def eventos(self, event):
        if event.type == pygame.KEYDOWN:
            self.scene = Jogo()

    def nextScene(self):
        return self.scene