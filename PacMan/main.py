import pgzrun

WIDTH = 512
HEIGHT = 512
BACKGROUND_COLOR = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

WALL_WIDTH = 64
WALL_HEIGHT = 64
PLAYER_SPEED = 64
""" 128 x 128"""

MAZE = [
    ["#","#","#","#","#","#","#","#"],
    ["#","@","#","","","","","#"],
    ["#","","#","#","","#","#","#"],
    ["#","","","","","","","#"],
    ["#","#","#","","#","#","#","#"],
    ["#","","","","","","","#"],
    ["#","","#","","","#","","#"],
    ["#","#","#","#","#","#","#","#"]
    ]
"""
wall = Actor('roadtexture_25')
"""
"""
print("hello1")
def draw_wall(level, sprite):
    print("hello3")
    x_pos = 50
    y_pos = 50
    for i in range level:
        if i == "#":
            print("hello")
            x_pos = x_pos + i * 128
            wall.x = x_pos
            print(wall.x)
            wall.y = y_pos
            print(wall.y)
            wall.draw()
"""
pacman = Actor('platformpack_tile012', anchor=('left', 'top'))
pacman.x = 64
pacman.y = 64


def on_key_up(key):
    if key == keys.RIGHT:
        if pacman.x + PLAYER_SPEED < WIDTH:
            pacman.x += PLAYER_SPEED
    
    if key == keys.LEFT:
        if pacman.x + PLAYER_SPEED > 0 + PLAYER_SPEED:
            pacman.x -= PLAYER_SPEED
    
    if key == keys.UP:
        if pacman.y + PLAYER_SPEED > 0 + PLAYER_SPEED:
            pacman.y -= PLAYER_SPEED

    if key == keys.DOWN:
        if pacman.y + PLAYER_SPEED < HEIGHT:
            pacman.y += PLAYER_SPEED
        


def draw():
    screen.fill(BACKGROUND_COLOR)

    for i in range(len(MAZE)):
        row = MAZE[i]
        for j in range(len(row)):
            tile = row[j]
            if tile == "#":
                screen.blit('platformpack_tile007', (j * WALL_WIDTH, i*WALL_HEIGHT ))
                
    
    pacman.draw()



def update():
    

    
    """
    for i in range (len(LEVELS)):
        if LEVELS[i] == "#":
            print("hello")
            wall.left = x_pos
            print(wall.x)
            wall.y = y_pos
            wall.draw()
            x_pos = x_pos + WALL_WIDTH
            print(x_pos)
    """


pgzrun.go()