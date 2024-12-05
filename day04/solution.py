directions = [
    (0,1),   #right
    (0,-1),  #left
    (1,0),   #up
    (-1,0),  #down
    (1,1),   #top-right
    (1,-1),  #top-left
    (-1,1),  #bottom-right
    (-1,-1), #bottom-left
]

def readFile(textfile):
    file = open(textfile, "r")
    puzzle = []
    while True:
        content=file.readline()
        if not content:
            break
        puzzle.append(list(content))
    return puzzle

def isValid(x, y, max_x, max_y):
    return 0<=x<max_x and 0<=y<max_y

def foundWord(x, y, dx, dy, word, puzzle):
    for i in range(len(word)):
        nx, ny = x + i * dx, y + i * dy
        if not isValid(nx, ny, len(puzzle), len(puzzle[0])):
            return False
        if puzzle[nx][ny] != word[i]:
            return False
    return True

def foundMAS(x, y, puzzle):
    if puzzle[x][y] == "A":
        ax1, ay1, ax2, ay2 = x-1, y-1, x+1, y+1
        bx1, by1, bx2, by2 = x+1, y-1, x-1, y+1
        if isValid(ax1, ay1, len(puzzle), len(puzzle[0])) and isValid(ax2, ay2, len(puzzle), len(puzzle[0])) and isValid(bx1, by1, len(puzzle), len(puzzle[0])) and isValid(bx2, by2, len(puzzle), len(puzzle[0])):
            if (puzzle[ax1][ay1] == "M" and puzzle[ax2][ay2] == "S") and (puzzle[bx1][by1] == "M" and puzzle[bx2][by2] == "S"):
                return True
            if (puzzle[ax1][ay1] == "M" and puzzle[ax2][ay2] == "S") and (puzzle[bx1][by1] == "S" and puzzle[bx2][by2] == "M"):
                return True
            if (puzzle[ax1][ay1] == "S" and puzzle[ax2][ay2] == "M") and (puzzle[bx1][by1] == "M" and puzzle[bx2][by2] == "S"):
                return True
            if (puzzle[ax1][ay1] == "S" and puzzle[ax2][ay2] == "M") and (puzzle[bx1][by1] == "S" and puzzle[bx2][by2] == "M"):
                return True
    return False



puzzle = readFile("input.txt")
count = 0
mas_count = 0
for x in range(len(puzzle)):
    for y in range(len(puzzle[x])):
        if foundMAS(x, y, puzzle):
            mas_count+=1
        for dx, dy in directions:
            if foundWord(x, y, dx, dy, "XMAS", puzzle):
                count+=1

print("Solution Part 1: " + str(count))
print("Solution Part 2: " + str(mas_count))