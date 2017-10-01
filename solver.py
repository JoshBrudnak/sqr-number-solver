grid1 = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

   # grid2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
   #         [0, 0, 0, 0, 0, 3, 0, 8, 5],
   #         [0, 0, 1, 0, 2, 0, 0, 0, 0],
   #         [0, 0, 0, 5, 0, 7, 0, 0, 0],
   #         [0, 0, 4, 0, 0, 0, 1, 0, 0],
   #         [0, 9, 0, 0, 0, 0, 0, 0, 0],
   #         [5, 0, 0, 0, 0, 0, 0, 7, 3],
   #         [0, 0, 2, 0, 1, 0, 0, 0, 0],
   #         [0, 0, 0, 0, 4, 0, 0, 0, 9]]
import json




def findFreePosition(grid):
    for y in range(9):
        for x in range(9):
            if (grid[y][x] == 0):
                position = (y, x)
                return position
    return False

def saySolved(solved):
    solved = True


def isCollision(grid, position, value):
    for y in range(9):
        if grid[y][position[1]] == value:
            return True

    for x in range(9):
        if grid[position[0]][x] == value:
            return True

    row = position[0]
    col = position[1]
    yrange = range(0, 1)
    xrange = range(0, 1)

    if row < 3 and col < 3:
        yrange = range(0, 3)
        xrange = range(0, 3)
    elif row < 3 and col < 6:
        yrange = range(0, 3)
        xrange = range(3, 6)
    elif row < 3 and col >= 6:
        yrange = range(0, 3)
        xrange = range(6, 9)
    elif row < 6 and col < 3:
        yrange = range(3, 6)
        xrange = range(0, 3)
    elif row < 6 and col < 6:
        yrange = range(3, 6)
        xrange = range(3, 6)
    elif row < 6 and col >= 6:
        yrange = range(3, 6)
        xrange = range(6, 9)
    elif row >= 6 and col < 3:
        yrange = range(6, 9)
        xrange = range(0, 3)
    elif row >= 6 and col < 6:
        yrange = range(6, 9)
        xrange = range(3, 6)
    else:
        yrange = range(6, 9)
        xrange = range(6, 9)

    for y in yrange:
        for x in xrange:
            if grid[y][x] == value:
                return True

    return False



def solvePuzzle(grid, solved):
    position = findFreePosition(grid)

    if not position:
        return True

    for val in range(1, 10):
        if not isCollision(grid, position, val):
            grid[position[0]][position[1]] = val

            if solvePuzzle(grid, solved):
                return True

            grid[position[0]][position[1]] = 0

    return False


def getSolution(grid):
    solved = False
    solvePuzzle(grid, solved)
    #printGrid(grid)
    return grid

def getJsonSolution(grid):
    stuff = json.dumps(grid)
    print(stuff)

getSolution(grid1)
getJsonSolution(grid1)

theGrid = grid1