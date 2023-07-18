import pygame
from scripts.persons.Nave import Nave
from scripts.persons.Inimigo import Inimigo
from scripts.utils.Text import Text
from scripts.utils.constants import *
from scripts.scenes.GameOver import GameOver
from scripts.persons.Planet import Planet

class Jogo():
    def __init__(self):
        self.scene = self
        self.display = pygame.display.get_surface()
        self.all_sprites = pygame.sprite.Group()
        self.inimigos_sprites = pygame.sprite.Group()

        self.player = Nave(
            (600,600),
            [self.all_sprites]
        )

        self.tempo = 0

        self.som = pygame.mixer.Sound("assets/Sounds/bg.ogg")
        self.som.play(-1)


    def reiniciar(self):
        self.scene = self
        self.som.stop()
        self.som.play(-1)
        self.all_sprites.clear(self.display, self.display)
        self.all_sprites = pygame.sprite.Group()
        self.player = Nave(
            (600,600),
            [self.all_sprites]
        )

        self.tempo = 0
        return self


    def criarInimigo(self):
        self.tempo += 1
        if self.tempo == 60:
            Inimigo([self.all_sprites, self.inimigos_sprites])
        elif self.tempo == 100:
            Inimigo([self.all_sprites, self.inimigos_sprites])
            Inimigo([self.all_sprites, self.inimigos_sprites])
            Planet([self.all_sprites])
            self.tempo = 0

    def colisao(self):
        for inimigo in self.inimigos_sprites:
            if inimigo.rect.colliderect(self.player.rect):
                inimigo.kill()
                self.player.vida -= 1
                self.player.som.play()
                if self.player.vida == 0:
                    self.som.stop()
                    self.scene = GameOver(self.player.score, self)

        for tiro in self.player.tiro_sprite:
            for inimigo in self.inimigos_sprites:
                if tiro.rect.colliderect(inimigo.rect):
                    tiro.kill()
                    inimigo.dano(self.all_sprites)
                    self.player.score += 10

    def update(self):
        self.colisao()
        self.player.update()
        self.criarInimigo()
        self.all_sprites.update()

    def draw(self):
        Text(
            "Score:" + str(self.player.score),
            BRANCO,
            30
        ).draw([TELA_LARGURA - 200, 10])
        Text("Vida:" + str(self.player.vida),BRANCO,30).draw([10, 10])
        self.all_sprites.draw(self.display)

    def eventos(self, event):
        pass

    def nextScene(self):
        return self.scene