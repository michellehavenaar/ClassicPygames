import pygame
import sys


pygame.init()



SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
MAZE_WIDTH = 600
MAZE_HEIGHT = 600
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BACKGROUND_COLOR = (0, 0, 0)

player_image = pygame.image.load(r"/home/miescodes/Documents/projects/ClassicPygames/PacMan/pac.png")
block_image = pygame.image.load(r"/home/miescodes/Documents/projects/ClassicPygames/PacMan/brick.png")

maze = [
    ["#","#","#","#","#","#","#","#","#","#"],
    ["#",".",".",".",".",".",".",".",".","#"],
    ["#",".","#","#","#","#","#","#",".","#"],
    ["#",".",".",".",".",".",".","#",".","#"],
    ["#",".","#",".","#",".",".",".",".","#"],
    ["#",".","#",".","#",".","#","#",".","#"],
    ["#",".","#",".","#",".",".",".",".","#"],
    ["#",".","#",".",".",".","#","#",".","#"],
    ["#",".",".",".","#",".",".",".",".","#"],
    ["#","#","#","#","#","#","#","#","#","#"]
]

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 5

    def draw(self, screen):
        screen.blit(player_image, (self.x, self.y))

class block(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def draw(self, screen, maze):
        for i in range(len(maze)):
            row = maze[i]
            for j in range(len(row)):
                tile = row[j]
                if tile == "#":
                    screen.blit(block_image, (j * self.width, i * self.height))


screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption("PACMAN")



# functions

def draw_game():
    screen.fill((BACKGROUND_COLOR))
    brick.draw(screen, maze)
    pac.draw(screen)
    pygame.display.update()



# game loop
pac = player(300, 300, 64, 64)
brick = block(64, 64)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if pac.x - pac.velocity > 0:
            pac.x -= pac.velocity

    if keys[pygame.K_RIGHT]:
        if pac.x + pac.velocity < SCREEN_WIDTH - pac.width:
            pac.x += pac.velocity

    if keys[pygame.K_UP]:
        if pac.y - pac.velocity > 0:
            pac.y -= pac.velocity
    
    if keys[pygame.K_DOWN]:
        if pac.y + pac.velocity < SCREEN_HEIGHT - pac.height:
            pac.y += pac.velocity
    
    draw_game()

pygame.quit()
    
    
