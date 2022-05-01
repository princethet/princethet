#conway's life of death
import random, time, copy
WIDTH = 60
HEIGHT = 20

#Create a list of list for the cells:
nextCells = []
for x in range(WIDTH):
    column = [] # create a new column.
    for y in range(HEIGHT):
        if (x,y) in ((1,0), (2,1), (0,2), (1,2), (2,2)):
            column.append('#') # Add a living cell.
        else:
            column.append(' ') # Add a dead cell.
    nextCells.append(column) # nextCell is a list of column lists.

while True: # Main program loop.
    print('\n\n\n\n\n') # Separate each step with newlines.
    currentCells = copy.deepcopy(nextCells)

    #print currentCells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') # Print the # or space.
        print() #Print a newline at the end of the row.

    #calculate the next step's cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            #get neighboring coordinates:
            # % width ensures leftcoord is always between 0 and width -1
            leftCoord = (x-1)%WIDTH
            rightCoord = (x+1)%WIDTH
            aboveCoord = (y-1)%HEIGHT
            belowCoord = (y+1)%HEIGHT

            # count number of living neighbors:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 #Top-left neighbor is alive.
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 #top neighbor is alive.
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 #top-right neighbor is alive 
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1 #left neighbor is alive.
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1 # right neighbor is alive.
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # bottom-left neighbor is alive.
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 # bottom neighbor is alive.
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 # bottom-right neighbor is alive.


            # Set cell based on Conway's Game of life rules:
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                #living cells with 2 or 3 neighbors stay alive:
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # DEAD cells with neighbors become alive:
                nextCells[x][y] = '#'
            else:
                # everythings else dies or stays dead:
                nextCells[x][y] = ' '
        time.sleep(1)