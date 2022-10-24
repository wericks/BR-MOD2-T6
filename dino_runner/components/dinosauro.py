import pygame

from dino_runner.utils.constants import RUNNING, JUMPING

# constant para uso global 
X_POS = 80
Y_POS = 301
JUMP_VEL = 8.5
class Dinosauro:
    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.dino_jump_vel = JUMP_VEL
    # Metodo de atulizacao das acoes no jogo
    def update(self, user_input):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.dino_jump()

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
        elif not self.dino_jump:
            self.dino_jump = False 
            self.dino_run = True

        if self.step_index >= 10:
            self.step_index = 0

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1] # condição if reduzida
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        
    def draw(self, screen): # screen para saber onde desenhar
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def jump(self):
        self.image = JUMPING
        if self.dino_jump:
            self.dino_rect.y -= self.dino_jump_vel * 4
            self.dino_jump_vel -= 0.8

        if self.dino_jump_vel < -JUMP_VEL:
            self.dino_rect.y = Y_POS 
            self.dino_jump = False
            self.dino_jump_vel - JUMP_VEL
