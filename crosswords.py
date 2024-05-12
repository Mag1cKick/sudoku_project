ways = []

def checkHorizontal(x, y, grid, currentWord):
    n = len(currentWord)

    for i in range(n):
        if grid[x][y + i] == '-' or grid[x][y + i] == currentWord[i]:
            grid[x] = grid[x][:y + i] + currentWord[i] + grid[x][y + i + 1:]
        else:
            grid[0] = "@"
            return grid
    return grid

def checkVertical(x, y, grid, currentWord):
    n = len(currentWord)

    for i in range(n):
        if grid[x + i][y] == '-' or grid[x + i][y] == currentWord[i]:
            grid[x + i] = grid[x + i][:y] + currentWord[i] + grid[x + i][y + 1:]
        else:
            grid[0] = "@"
            return grid
    return grid

def solvePuzzle(words, grid, index, n):
    global ways
    if index < len(words):
        currentWord = words[index]
        maxLen = n - len(currentWord)
        for i in range(n):
            for j in range(maxLen + 1):
                temp = checkVertical(j, i, grid.copy(), currentWord)
                if temp[0] != "@":
                    solvePuzzle(words, temp, index + 1, n)
        for i in range(n):
            for j in range(maxLen + 1):
                temp = checkHorizontal(i, j, grid.copy(), currentWord)
                if temp[0] != "@":
                    solvePuzzle(words, temp, index + 1, n)
    else:
        ways.append(grid)

def solvecross(words, grid, index, n):
    solvePuzzle(words, grid, index, n)
    for i, j in enumerate(ways):
        i=i+1000000000001
        print(f"{i-1000000000000}{'st' if int(str(i)[-1]) == 1 and int(str(i)[-1] + str(i)[-2])!= 11 else 'nd' if int(str(i)[-1]) == 2 and int(str(i)[-1] + str(i)[-2])!= 12 else 'rd' if int(str(i)[-1]) == 3 and int(str(i)[-1] + str(i)[-2])!= 13 else 'th'} way to solve")
        print('\n'.join(j))
        print()
if __name__ == '__main__':
    n1 = 10
    grid = []

    grid.append("*-********")
    grid.append("*-********")
    grid.append("*-****-***")
    grid.append("*--***--**")
    grid.append("*-****-***")
    grid.append("*-****-***")
    grid.append("*-****-***")
    grid.append("*-*------*")
    grid.append("*-********")
    grid.append("***-------")

    words = []

    words.append("PUNJAB")
    words.append("JHARKHAND")
    words.append("MIZORAM")
    words.append("MUMBAI")

    solvecross(words, grid, 0, n1)
    print("Number of ways to fill the grid is " + str(len(ways)))