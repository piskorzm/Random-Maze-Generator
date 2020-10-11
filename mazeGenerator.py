import pygame
import random
import time
import copy

pygame.init()
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0, 255, 0)

window_w = 2000
window_h = 1000
block = 4

rows = int(window_w/block)
cols = int(window_h/block)

positions = [[False for col in range(cols)] for row in range(rows)]

start = [0, random.choice(range(cols-1))]
start1 = [1, start[1]]

end = [rows-1,0]

positions[start[0]][start[1]] = True
positions[start1[0]][start1[1]] = True

randompool = [start1]

def make_maze():
    e = 0
    while len(randompool)>0:
        add(random.choice(randompool))
        if (e % 500 == 0):
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
    return position[0] < 0 or position[0] >= rows or position[1] < 0 or position[1] >= cols or positions[position[0]][position[1]]

def valid(position,neighbour):
    up = [(position[0]-1),(position[1])]
    down = [(position[0]+1),(position[1])]
    left = [(position[0]),(position[1]-1)]
    right = [(position[0]),(position[1]+1)]
    upleft = [(position[0]-1),(position[1]-1)]
    upright = [(position[0]-1),(position[1]+1)]
    downleft = [(position[0]+1),(position[1]-1)]
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

    for i in range(rows):
        for j in range(cols):
            if positions[i][j]:
                pygame.draw.rect(gameDisplay, white, [i*block, j*block, block, block])

    pygame.draw.rect(gameDisplay, red, [start[0]*block, start[1]*block, block, block])
    pygame.draw.rect(gameDisplay, red, [end[0]*block, end[1]*block, block, block])
    pygame.display.update()

def generate_end():
    while(end[1] == 0):
        random_col = random.choice(range(cols-1))
        end[1] = random_col

        if (not occupied([end[0]-1, end[1]])):
            end[1] = 0
        else:
            positions[end[0]][end[1]] = True

def explore(previous_position, current_position):

    branch = [copy.copy(current_position)]

    nexts = []

    explored = False

    is_correct = False

    while(not explored):

        
            
        if (current_position[0] == end[0]):
            is_correct = True
            explored = True
            
        else:

            nexts = []

            up = [(current_position[0]-1),(current_position[1])]
            down = [(current_position[0]+1),(current_position[1])]
            left = [(current_position[0]),(current_position[1]-1)]
            right = [(current_position[0]),(current_position[1]+1)]

            if (up != previous_position and positions_solve[up[0]][up[1]]):
                nexts.append(up)
            if (down != previous_position and positions_solve[down[0]][down[1]]):
                nexts.append(down)
            if (left != previous_position and positions_solve[left[0]][left[1]]):
                nexts.append(left)
            if (right != previous_position and positions_solve[right[0]][right[1]]):
                nexts.append(right)

            

            if (len(nexts) == 0 or is_correct):
                explored = True
            elif (len(nexts) == 1):
                previous_position = copy.copy(current_position)
                current_position = nexts[0]
                branch.append(copy.copy(current_position))

                
                
                if (current_position[0] == end[0]):
                    is_correct = True

            else:
                is_correct = explore(current_position, nexts[random.choice(range(len(nexts)))])

    if (is_correct):
        for position in branch:
            path.append(position)
    else:
        for position in branch:
            positions_solve[position[0]][position[1]] = False 
    
    return is_correct

def print_path():
    for position in path:
        pygame.draw.rect(gameDisplay, red, [position[0]*block, position[1]*block, block, block])

    
    pygame.display.update()

gameExit = False

gameDisplay = pygame.display.set_mode((window_w,window_h))
pygame.display.set_caption('Maze Generator')

make_maze()

generate_end()
print_maze()

path = []
positions_solve = copy.deepcopy(positions)
explore(start, start1)

print_path()



print('Press q to quit')
gameExit = False
while gameExit == False:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            gameExit = True

pygame.quit()
quit()
