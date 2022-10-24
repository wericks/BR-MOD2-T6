from dino_runner.utils.constants import RUNNING

class Dinosauro:
    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = 80
        self.dino_rect.y = 310
        self.step_index = 0

    # Metodo de atulizacao das acoes no jogo
    def update(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1] # condição if reduzida
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = 80
        self.dino_rect.y = 310

        if self.step_index >= 10:
            self.step_index = 0
        

    def draw(self, screen): # screen para saber onde desenhar
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))