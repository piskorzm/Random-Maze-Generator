import pygame
import random
import time
pygame.init()
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

window_w = 1000
window_h = 1000
block = 5

cols = int(window_w/block)
rows = int(window_h/block)

positions = [[False for col in range(cols)] for row in range(rows)]

start = [0, random.choice(range(0,rows))]
start1 = [0, start[1]+1]

positions[start[0]][start[1]] = True
positions[start1[0]][start1[1]] = True

randompool = [start1]


possible = []

end = [0, start[1]]



def make_maze():
    e = 0
    while len(randompool)>0:
        add(random.choice(randompool))
        if (e % 200 == 0):
            print_maze()
        
        e+=1

def add(position):
    up = [position[0],position[1]-1]
    down = [position[0],position[1]+1]
    left = [position[0]-1,position[1]]
    right = [position[0]+1,position[1]]

    if occupied(up):
        neighbour=up
    elif occupied(down):
        neighbour=down
    elif occupied(left):
        neighbour=left
    elif occupied(right):
        neighbour=right
        
    branches = random.choice([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,3,3])

    possiblenexts=[up,down,left,right]

    validnexts = []
    for i in possiblenexts:
        if valid(i,neighbour):
            validnexts.append(i)

    while branches > 0 and len(validnexts) > 0:
        next_block=random.choice(validnexts)

        positions[next_block[0]][next_block[1]] = True

        randompool.append(next_block)

        validnexts.remove(next_block)

        branches-=1

    randompool.remove(position)

def occupied(position):
    print(position)
    return position[0] < 0 or position[0] >= rows or position[1] < 0 or position[1] >= cols or positions[position[0]][position[1]]

def valid(position,neighbour):
    up = [(position[0]),(position[1]-1)]
    down = [(position[0]),(position[1]+1)]
    left = [(position[0]-1),(position[1])]
    right = [(position[0]+1),(position[1])]
    upleft = [(position[0]-1),(position[1]-1)]
    upright = [(position[0]+1),(position[1]-1)]
    downleft = [(position[0]-1),(position[1]+1)]
    downright = [(position[0]+1),(position[1]+1)]

    if  position[0]<0 or position[0]>=rows or position[1]<0 or position[1]>=cols:
        return False

    n=0
    if occupied(up):
        n+=1
    if occupied(down):
        n+=1
    if occupied(left):
        n+=1
    if occupied(right):
        n+=1

    if n>1:
        return False
    if occupied(upleft) and upleft != neighbour:
        return False
    if occupied(upright) and upright != neighbour:
        return False
    if occupied(downleft) and downleft != neighbour:
        return False
    if occupied(downright) and downright != neighbour:
        return False

    return True

def print_maze():
    gameDisplay.fill(black)

    pygame.draw.rect(gameDisplay, red, [start[0]*block, start[1]*block, block, block])

    for i in range(len(positions)):
        for j in range(len(positions[i])):
            if positions[i][j]:
                pygame.draw.rect(gameDisplay, white, [i*block, j*block, block, block])

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

make_maze()

print_maze()

print('Press q to quit')
gameExit = False
while gameExit == False:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            gameExit = True

pygame.quit()
quit()
