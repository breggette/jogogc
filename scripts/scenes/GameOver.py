import pygame
from scripts.utils.constants import *
from scripts.utils.Text import Text

class GameOver():
    def __init__(self, score, jogo):
        self.scene = self
        self.display = pygame.display.get_surface()
        self.score = score
        self.jogo = jogo

    def update(self):
        pass

    def draw(self):
        Text("GAME OVER", BRANCO, 50).drawCenter()
        Text(
            "Você fez " + str(self.score) + " pontos",
            BRANCO,
            30
        ).draw([
            (TELA_LARGURA / 2) - 100,
            (TELA_ALTURA / 2) + 60
        ])

    def eventos(self, event):
        if event.type == pygame.KEYDOWN:
            self.scene = self.jogo.reiniciar()

    def nextScene(self):
        return self.scene