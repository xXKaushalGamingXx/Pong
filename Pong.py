#imports
import pygame

#window
pygame.init()
window = pygame.display.set_mode((840, 640))
pygame.display.set_caption("Simple Pong")
background = pygame.transform.scale(pygame.image.load("background.png"), (840, 640))

#variables
ball_speed_y = 3
ball_speed_x = 3
player1_score = 0
player2_score = 0

#classes
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (22, 100))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player_1(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
class Player_2(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
class Ball(GameSprite):
    def update(self):
        global ball_speed_x, ball_speed_y, player1_score, player2_score
        self.rect.x += ball_speed_x
        self.rect.y += ball_speed_y
        #Collision with walls
        if self.rect.top <= 0 or self.rect.bottom >= 640:
            ball_speed_y = -ball_speed_y
        #Collision with paddles
        if self.rect.colliderect(Player1.rect) or self.rect.colliderect(Player2.rect):
            ball_speed_x = -ball_speed_x
        #collision with walls
        if self.rect.left <= 0:
            player2_score += 1
            self.rect.center = (420, 320)
            ball_speed_x = -ball_speed_x
        if self.rect.right >= 840:
            player1_score += 1
            self.rect.center = (420, 320)
            ball_speed_x = -ball_speed_x

#gui
font = pygame.font.Font(None, 36)
text_left = font.render(str(player1_score), True, (255, 255, 255))
text_right = font.render(str(player2_score), True, (255, 255, 255))

#creation of sprites
Player1 = Player_1("Paddle_1_copy.png", 30, 324, 5)
Player2 = Player_2("Paddle_2_copy.png", 790, 324, 5)
BallObject = Ball("Pong_ball.png", 220, 320, 5)
#fps control
clock = pygame.time.Clock()
FPS = 60

#gameloop
game = True
while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
    #background
    window.blit(background,(0,0))
    #gui
    window.blit(text_left, (100, 10))
    window.blit(text_right, (740, 10))
    #player 1
    Player1.reset()
    Player1.update()
    #player
    Player2.reset()
    Player2.update()
    #ball
    BallObject.reset()
    BallObject.update()
    # update scores
    text_left = font.render(str(player1_score), True, (255, 255, 255))
    text_right = font.render(str(player2_score), True, (255, 255, 255))
    #stuff
    clock.tick(FPS)
    pygame.display.update()