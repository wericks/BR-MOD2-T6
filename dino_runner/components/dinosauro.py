import pygame
# 1 linha vazia entre imports 
from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING

# constant para uso global 
X_POS = 80
Y_POS = 310
JUMP_VEL = 8.5
# 2 linhas para classe inicio
class Dinosauro(Sprite):
    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.jump_vel = JUMP_VEL
        self.dino_duck = False
    # Metodo de atulizacao das acoes no jogo # 1 linha para metodos
    def update(self, user_input):

        if self.step_index >= 10:
            self.step_index = 0
        # 1 linha entre blocos de logica
        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True 
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or self.dino_duck): # valide os mesmos tipos 
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False 

        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1] # condição if reduzida
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index += 1
        
    def draw(self, screen): # screen para saber onde desenhar
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def jump(self):
        self.image = JUMPING
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8

        if self.jump_vel < -JUMP_VEL:
            self.dino_rect.y = Y_POS 
            self.dino_jump = False
            self.jump_vel = JUMP_VEL

    def duck(self):
        self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS + 59 # + pro dino nao ficar voando
        # self.dino_rect.y = Y_POS * 2  # dino teleporta
        self.step_index += 1
        self.dino_duck = False # permite que nao trave no posicao duck
