import pygame
from scripts.utils.Obj import Obj
from scripts.utils.constants import *
from scripts.elements.Tiro import Tiro

class Nave(Obj):
    def __init__(self, pos, *groups):
        super().__init__("assets/nave/nave0.png", pos, *groups)
        self.direct = pygame.math.Vector2(pos[0], pos[1])
        self.speed = 7
        self.vida = 3
        self.tempo_tiro = 0
        self.score = 0
        self.group = groups

        # Grupo para os tiros
        self.tiro_sprite = pygame.sprite.Group()

        # som de dano
        self.som = pygame.mixer.Sound("assets/sounds/damage.ogg")

    def input(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w] or key[pygame.K_UP]:
            self.direct.y -= self.speed
        if key[pygame.K_s] or key[pygame.K_DOWN]:
            self.direct.y += self.speed
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            self.direct.x -= self.speed
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            self.direct.x += self.speed

        if key[pygame.K_SPACE]:
            if self.tempo_tiro >= 50:
                self.tempo_tiro = 0
                posX = self.rect.x + self.image.get_width() / 2
                posY = self.rect.y - 30
                Tiro((posX, posY), [self.tiro_sprite, self.group])

    def move(self):
        self.rect.center = self.direct

    def limit(self):
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > TELA_LARGURA - self.image.get_width():
            self.rect.x = TELA_LARGURA - self.image.get_width()

        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > TELA_ALTURA - self.image.get_height():
            self.rect.y = TELA_ALTURA - self.image.get_height()

    def update(self):

        if self.score <= 300:
            super().animate(5, [
                "assets/nave/nave0.png",
                "assets/nave/nave1.png",
                "assets/nave/nave2.png"
            ])
        else:
            self.naveMonstra()

        self.tempo_tiro += 1
        self.input()
        self.move()
        self.limit()

    def naveMonstra(self):
        speed = 5
        imgs = [
            "assets/minhaNave/minhaNave1.png",
            "assets/minhaNave/minhaNave2.png",
            "assets/minhaNave/minhaNave3.png"
        ]

        self.tick += 1

        if self.tick > speed:
            self.tick = 0
            self.frame = (self.frame + 1) % len(imgs)
            self.image = pygame.image.load(imgs[self.frame])
            self.image = pygame.transform.scale(self.image, (110, 117))
