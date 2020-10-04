import sys, pygame
from time import sleep
from random import randint

##game parameters
size = 500
numcell = 50
gamespeed = 0.05

def getpos(pos):
    return (pos-1)*(size/numcell)

pygame.init()
done = False
screen = pygame.display.set_mode((size,size))
carl = [(1,1)]
direc = (0,0)
foodp = False
ap = False
move = 0

while not done:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        #set direction
        if event.type == pygame.KEYDOWN:
            print(1)
            if event.key == pygame.K_LEFT or move == 1:
                direc = (-1, 0)
            elif event.key == pygame.K_RIGHT or move == 2:
                direc = (1, 0)
            elif event.key == pygame.K_UP or move == 3:
                direc = (0, -1)
            elif event.key == pygame.K_DOWN or move == 4:
                direc = (0, 1)
    #check presence of food ans spawn food if needed
    if not foodp:
        food = (randint(0,numcell), randint(0,numcell))
        foodp = True
    #draw food
    pygame.draw.rect(screen, (255, 0, 0), (getpos(food[0]), getpos(food[1]), size / numcell, size / numcell))
    #run snake updates
    carl.insert(0,tuple(map(sum, zip(carl[0], direc))))
    if not ap:
        carl.pop()
    ap = False
    #draw carl
    for i in carl:
        pygame.draw.rect(screen, (255,255,255), (getpos(i[0]), getpos(i[1]),size/numcell, size/numcell))
    #check death
    if getpos(carl[0][1]) < 0 or getpos(carl[0][0]) < 0 or getpos(carl[0][1]) > size or getpos(carl[0][0]) > size or carl[0] in carl[1:len(carl)]:
        done = True
    #check food after position update
    if carl[0] == food:
        ap = True
        foodp = False
    sleep(gamespeed)
    pygame.display.update()


