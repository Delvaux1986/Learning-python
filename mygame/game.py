# IMPORTS 
import sys,pygame 
print(pygame)
pygame.init()
# print("{0} successes and {1} failures".format(successes, failures))

# DISPLAY 
screen = pygame.display.set_mode((1024,768 ))
clock = pygame.time.Clock()
FPS = 60 
# VARIABLE & CONST COLOR
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# SETUP OF GAME
pygame.mouse.set_visible(1)
# ELEM OF GAME
rect = pygame.Rect((0, 0), (32, 32)) 
image = pygame.Surface((32, 32))
image.fill(WHITE)
pygame.display.set_caption('MyGame')
# BG IMG
bg = pygame.image.load('./space1024.jpg')
# SHIP
size = (100,50)
circle = pygame.Surface(size)
radius = int(50)




         
# WHILE OF GAME 
while True:
    clock.tick(FPS)
    screen.blit(bg,(0,0))
    pygame.draw.circle(screen, WHITE ,(radius, radius), radius, 5)
    pygame.display.flip()
    pygame.display.update() 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    
pygame.quit()