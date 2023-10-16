import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
WINDOW_SIZE = (WIDTH, HEIGHT)
WINDOW_TITLE = "Snake Game"
FPS = 10

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(WINDOW_TITLE)


# creation of snake

class Snake(): 

    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height)) 


# creation of food

class Food():
    
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.x = random.randrange(0, 800, 1)
        self.y = random.randrange(0, 600, 1)
        self.width = width
        self.height = height
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        

direction_x = 1
direction_y = 0
step = 15

running = True
clock = pygame.time.Clock()

snake_obj = Snake(20, 20, 45, 45, GREEN)
food_obj = Food(20, 20, 45, 45, RED)


# game rules

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN] and direction_y == 0:
        direction_y += step
        direction_x = 0
    if keys[pygame.K_UP] and direction_y == 0:
        direction_y -= step
        direction_x = 0
    if keys[pygame.K_RIGHT] and direction_x == 0:
        direction_x += step
        direction_y = 0
    if keys[pygame.K_LEFT] and direction_x == 0:
        direction_x -= step
        direction_y = 0
    if snake_obj.rect.colliderect(food_obj.rect):
        snake_obj.rect.width += 45
        snake_obj.rect.height += 45

    

    snake_obj.x += direction_x
    snake_obj.y += direction_y
    
    screen.fill(WHITE)
    snake_obj.draw(screen)
    food_obj.draw(screen)
    pygame.display.update()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()

