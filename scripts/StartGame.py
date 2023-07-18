import pygame
from scripts.utils.constants import *
from scripts.scenes.Inicial import Inicial
from scripts.utils.BgAnimado import BgAnimado

class StartGame():
    def __init__(self):
        # Inicializa o pygame
        pygame.init()

        # Inicializa a tela
        self.display = pygame.display.set_mode(
            (TELA_LARGURA, TELA_ALTURA)
        )

        # Inicializa o título
        pygame.display.set_caption('Space Ship')

        # Cena
        self.sceneObj = Inicial()

        # Inicializa o relógio
        self.fps = pygame.time.Clock()

        # Inicializa o loop principal
        self.jogando = True

        # Chama o objeto do fundo animado
        self.Bg = BgAnimado()


    def run(self):
        # Loop principal
        while self.jogando:

            # Verifica qual a cena atual
            self.sceneObj = self.sceneObj.nextScene()

            # Eventos
            for event in pygame.event.get():
                self.sceneObj.eventos(event)

                # Fecha o jogo se apertar no X
                if event.type == pygame.QUIT:
                    self.jogando = False

                # Verifica se apertou alguma tecla
                if event.type == pygame.KEYDOWN:

                    # Fecha o jogo se apertar ESC
                    if event.key == pygame.K_ESCAPE:
                        self.jogando = False

            self.display.fill(PRETO)
            self.Bg.draw()
            self.sceneObj.update()
            self.sceneObj.draw()

            self.fps.tick(60)
            pygame.display.flip()