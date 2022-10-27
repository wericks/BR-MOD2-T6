import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosauro import Dinosauro
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

FONT_STYLE = 'freesansbold.ttf'
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.score = 0 
        self.death_count = 0
        self.player = Dinosauro() # player instancia da classe 
        self.obstacle_manager = ObstacleManager()
        self.message = ""

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obtacles()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()

    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 5

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen) # chama o parametro para usar para desenha na tela
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        self.message = "Pontos: " + str(self.score)
        self.draw_text(self.message, 1000, 50)

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.score = 0
                self.run()

    def show_menu(self):
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH //2

        if self.death_count == 0:
            self.message = "Pressione alguma tecla"
            self.draw_text(self.message, half_screen_width, half_screen_height)
        elif self.death_count > 0 :
            self.game_speed = 20
            # "Press any key to restart"
            self.message = "Precione uma tecla para reconeçar"
            self.draw_text(self.message, half_screen_width, half_screen_height)

            self.message = "Sua Pontuação: " + str(self.score)
            self.draw_text(self.message, half_screen_width + 30, half_screen_height + 30)

            self.message = "Mortes: " + str(self.death_count)
            self.draw_text(self.message, half_screen_width + 30, half_screen_height + 60)
            
            
            
 
        # else:
            
        #     # score atingido
        #     self.message = "Pontuação: + str(self.score"
        #     self.draw_text(self.message, half_screen_width // 3, half_screen_height // 3)

        #     # resetar game_speed e score
        #     self.game_speed = 20
        #     self.death_count += 1
        #     self.message = f"Mortes {self.death_count}"
        #     self.draw_text(self.message, half_screen_width + 45, half_screen_height + 45)
            
        #     # death_count
            
        #     self.screen.blit(ICON, (half_screen_width - 20, half_screen_height - 140))

        pygame.display.update()
        self.handle_events_on_menu()


    def draw_text(self, message, screen_width, screen_height):
        ## método reutilizável para desenhar os textos
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(message, True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (screen_width, screen_height)
        self.screen.blit(text, text_rect)