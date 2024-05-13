ways = []

def hor_ch(x, y, grid, word):
    """places words horisontaly"""
    n = len(word)
    for i in range(n):
        if grid[x][y + i] == '-' or grid[x][y + i] == word[i]:
            grid[x] = grid[x][:y + i] + word[i] + grid[x][y + i + 1:]
        else:
            grid[0] = "1"
            return grid
    return grid

def ver_ch(x, y, grid, word):
    """places words verticaly"""
    n = len(word)
    for i in range(n):
        if grid[x + i][y] == '-' or grid[x + i][y] == word[i]:
            grid[x + i] = grid[x + i][:y] + word[i] + grid[x + i][y + 1:]
        else:
            grid[0] = "1"
            return grid
    return grid

def placements(words, grid, index, v, h):
    """finds all possible ways to fit words in the grid"""
    global ways
    if index < len(words):
        curr = words[index]
        v_len = v - len(curr)
        h_len = h - len(curr)
        for i in range(h):
            for j in range(v_len + 1):
                a = ver_ch(j, i, grid.copy(), curr)
                if a[0] != "1":
                    placements(words, a, index + 1, v, h)
        for i in range(v):
            for j in range(h_len + 1):
                a = hor_ch(i, j, grid.copy(), curr)
                if a[0] != "1":
                    placements(words, a, index + 1, v, h)
    else:
        ways.append(grid)

def solvecross(words, grid, index, v, h):
    placements(words, grid, index, v, h)
    for i, j in enumerate(ways):
        i=i+1000000000001
        print(f"{i-1000000000000}{'st' if int(str(i)[-1]) == 1 and int(str(i)[-1] + str(i)[-2])!= 11 else 'nd' if int(str(i)[-1]) == 2 and int(str(i)[-1] + str(i)[-2])!= 12 else 'rd' if int(str(i)[-1]) == 3 and int(str(i)[-1] + str(i)[-2])!= 13 else 'th'} way to solve")
        print('\n'.join(j))
        print()
if __name__ == '__main__':
    n1 = 10
    grid = []

    grid.append("*-*********")
    grid.append("*-*********")
    grid.append("*-****-****")
    grid.append("*--***--***")
    grid.append("*-****-****")
    grid.append("*-****-****")
    grid.append("*-****-****")
    grid.append("*-*------**")
    grid.append("*-*********")
    grid.append("***-------*")

    words = []

    words.append("PUNJAB")
    words.append("JHARKHAND")
    words.append("MIZORAM")
    words.append("MUMBAI")

    solvecross(words, grid, 0, 10, 10)
    print("Number of ways to fill the grid is " + str(len(ways)))