import pygame
import random
import time
pygame.init()
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

window_w = 600
window_h = 350
block = 5




start = [0,random.choice(range(block,(window_h-block), block))]
start1 = [start[0]+block, start[1]]

end = [0, start[1]]

possible = []

maze = [start1]

randompool = [start1]


def make_list():
    for x in range(block,(window_h-block),block):
        for y in range(block,(window_w-block),block):
            possible.append([x,y])

def make_maze():

    while len(randompool)>0:
        print_maze()
        add(random.choice(randompool))

def add(position):
    up = [(position[0]),(position[1]-block)]
    down = [(position[0]),(position[1]+block)]
    left = [(position[0]-block),(position[1])]
    right = [(position[0]+block),(position[1])]

    neighbour=[]

    if up in maze:
        neighbour=up
    elif down in maze:
        neighbour=down
    elif left in maze:
        neighbour=left
    elif right in maze:
        neighbour=right
    branches = random.choice([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,3,3])

    possiblenexts=[up,down,left,right]

    validnexts = []
    for i in possiblenexts:
        if valid(i,neighbour)==True:
            validnexts.append(i)


    n=20

    while branches > 0 and len(validnexts) > 0:
        next_block=random.choice(validnexts)

        maze.append(next_block)

        randompool.append(next_block)

        validnexts.remove(next_block)

        branches-=1

    randompool.remove(position)


def valid(position,neighbour):
    up = [(position[0]),(position[1]-block)]
    down = [(position[0]),(position[1]+block)]
    left = [(position[0]-block),(position[1])]
    right = [(position[0]+block),(position[1])]
    upleft = [(position[0]-block),(position[1]-block)]
    upright = [(position[0]+block),(position[1]-block)]
    downleft = [(position[0]-block),(position[1]+block)]
    downright = [(position[0]+block),(position[1]+block)]

    if position[0]<block or position[0]>=window_w-block or \
       position[1]<block or position[1]>=window_h-block:
        return False

    n=0
    if up in maze:
        n+=1
    if down in maze:
        n+=1
    if left in maze:
        n+=1
    if right in maze:
        n+=1

    if n>1:
        return False
    if upleft in maze and upleft !=neighbour:
        return False
    if upright in maze and upright !=neighbour:
        return False
    if downleft in maze and downleft !=neighbour:
        return False
    if downright in maze and downright !=neighbour:
        return False

    else:

        return True

def print_maze():
    gameDisplay.fill(black)

    pygame.draw.rect(gameDisplay, red, [start[0], start[1], block, block])

    for position in maze:
        pygame.draw.rect(gameDisplay, white, [position[0], position[1], block, block])

    pygame.draw.rect(gameDisplay, red, [end[0], end[1], block, block])
    pygame.display.update()

def generate_end():
    global end

    for position in maze:

        if position[0] >= end[0]:
            end = [position[0] + block, position[1]]


gameExit = False

gameDisplay = pygame.display.set_mode((window_w,window_h))
pygame.display.set_caption('Maze Generator')

make_list()
make_maze()


generate_end()
print_maze()

print('Press q to quit')
gameExit = False
while gameExit == False:

    for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True

pygame.quit()
quit()
