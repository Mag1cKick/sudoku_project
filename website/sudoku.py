from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash
import random
from graphviz import Source
# from . import db
sudoku = Blueprint('sudoku', __name__)

@sudoku.route('/')
def main():
    return render_template('buttons.html')

@sudoku.route('/sud')
def sud():
    return render_template('sud.html')

@sudoku.route('/sud_res')
def sud_res():
    return render_template('sud_res.html')

@sudoku.route('/cros')
def cros():
    return render_template('cros.html')

@sudoku.route('/labirint')
def labirint():
    return render_template('labirint.html')

@sudoku.route('/graph')
def color():
    return render_template('graph.html')

def is_safe(board, row, col, num):
    for x in range(9):
        if board[row][x] == num:
            return False
    for x in range(9):
        if board[x][col] == num:
            return False
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + startRow][j + startCol] == num:
                return False
    return True






def solve_sudoku(board):
    find = find_empty_location(board)
    if not find:
        return True
    row, col = find
    for num in range(1, 10):
        if is_safe(board, row, col, num):
            board[row][col] = num
            # Рекурсивний виклик для наступної комірки
            if solve_sudoku(board):
                return True
            # Відкат, якщо рекурсивний виклик не веде до розв'язку
            board[row][col] = 0
    return False

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)  # Повертаємо координати першої незаповненої комірки
    return None

@sudoku.route('/solve_sudoku', methods=['POST', 'GET'])
def new_board():
    sudoku_data = request.json.get('sudoku_data')
    boardik = [int(i) for i in sudoku_data]
    board = []
    for i in range(0, len(boardik), 9):
        board.append(boardik[i:i+9])
    if solve_sudoku(board):
        # print(board[0][0])
        for i in range(len(board)):
            for j in range(len(board)):
                board[i][j] = str(board[i][j])
        a="\r"
        flash(f'{a.join("".join(i) for i in board)}', category='success')
    else:
        print("No solution exists")
    return render_template('sud_res.html', board=board)
# Приклад використання
# board = [
#     [5, 3, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9]
# ]

# if solve_sudoku(board):
#     for row in board:
#         print(row)
# else:
#     print("No solution exists")



class Maze:
    def __init__(self, grid) -> None:
        self.size = len(grid)
        self.maze = grid

    def exploreMaze(self, row, col):

        if self.maze[row][col]==2:
            #We found the exit
            return True

        elif self.maze[row][col]==0: #Empty path, not explored
            self.maze[row][col]=3

            if row<len(self.maze)-1:
                #Explore path below
                if self.exploreMaze(row+1,col):
                    return True

            if row>0:
                #Explore path above
                if self.exploreMaze(row-1,col):
                    return True

            if col<len(self.maze[row])-1:
                #Explore path to the right
                if self.exploreMaze(row,col+1):
                    return True

            if col>0:
                #Explore path to the left
                if self.exploreMaze(row,col-1):
                    return True

            #Backtrack
            self.maze[row][col]=4

            # print("Backtrack")

maze_3 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
          [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
          [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
          [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
          [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
          [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
          [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
          [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
          [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
          [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
          [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
          [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
          [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
          [1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

maze_solver = Maze(maze_3)
# print(maze_solver.exploreMaze(1, 1))

@sudoku.route("/maze_solver", methods=["POST"])
def solve_maze_route():
    data = request.json
    maze_data = data["maze"]
    start_coords = data["startCoords"]

    # Solve the maze
    solved_maze = Maze(maze_data)
    result = solved_maze.exploreMaze(start_coords["row"], start_coords["col"])

    if result:
        # Maze solved
        print(solved_maze.maze)
        return jsonify({"message": "Maze solved successfully"}, {"new_maze": solved_maze.maze})

    else:
        # Maze cannot be solved
        return jsonify({"message": "Maze cannot be solved"})





ways = []
class cross1:
    def __init__(self, grid, words) -> None:
        self.grid = grid
        self.words = words
        self.ways = []

    @staticmethod
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

    @staticmethod
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

    def placements(self, grid, index, v, h):
        """finds all possible ways to fit words in the grid"""
        if index < len(self.words):
            curr = self.words[index]
            v_len = v - len(curr)
            h_len = h - len(curr)
            for i in range(h):
                for j in range(v_len + 1):
                    a = self.ver_ch(j, i, grid.copy(), curr)
                    if a[0] != "1":
                        self.placements(a, index + 1, v, h)
            for i in range(v):
                for j in range(h_len + 1):
                    a = self.hor_ch(i, j, grid.copy(), curr)
                    if a[0] != "1":
                        self.placements(a, index + 1, v, h)
        else:
            self.ways.append(grid)


@sudoku.route('/solve', methods=['POST'])
def solve():
    global ways
    grid = [i.strip() for i in request.form['grid'].split('\n')]
    words = request.form.getlist('words')
    cros1 = cross1(grid, words)
    cros1.placements(grid, 0, len(grid), len(grid[0]))
    way = cros1.ways
    cros1.ways = []
    return render_template('cros_res.html', ways=enumerate(way))
# if __name__ == '__main__':
#     n1 = 10
#     grid = []

#     grid.append("*-*********")
#     grid.append("*-*********")
#     grid.append("*-****-****")
#     grid.append("*--***--***")
#     grid.append("*-****-****")
#     grid.append("*-****-****")
#     grid.append("*-****-****")
#     grid.append("*-*------**")
#     grid.append("*-*********")
#     grid.append("***-------*")

#     words = []

#     words.append("PUNJAB")
#     words.append("JHARKHAND")
#     words.append("MIZORAM")
#     words.append("MUMBAI")

#     solvecross(words, grid, 0, 10, 10)
#     print("Number of ways to fill the grid is " + str(len(ways)))




class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
        self.node_colors = [None] * num_vertices

    def add_edge(self, src, dest):
        self.adjacency_matrix[src][dest] = 1
        self.adjacency_matrix[dest][src] = 1

    def add_random_edges(self, num_edges):
        for _ in range(num_edges):
            src = random.randint(0, self.num_vertices - 1)
            dest = random.randint(0, self.num_vertices - 1)
            while src == dest or self.adjacency_matrix[src][dest] == 1:
                dest = random.randint(0, self.num_vertices - 1)
            self.add_edge(src, dest)

    def to_dot(self):
        dot_string = "graph G {\n"
        for i in range(self.num_vertices):
            if self.node_colors[i]:
                dot_string += f"    {i} [fillcolor=\"{self.node_colors[i]}\", style=filled];\n"

        for i in range(self.num_vertices):
            for j in range(i + 1, self.num_vertices):
                if self.adjacency_matrix[i][j] == 1:
                    dot_string += f"    {i} -- {j};\n"
        dot_string += "}\n"
        return dot_string

    def color_graph(self):
        colors = [-1] * self.num_vertices

        def is_safe(vertex, color):
            for i in range(self.num_vertices):
                if self.adjacency_matrix[vertex][i] == 1 and colors[i] == color:
                    return False
            return True

        def get_available_color(vertex):
            for color in range(self.num_vertices):
                if is_safe(vertex, color):
                    return color

        for vertex in range(self.num_vertices):
            colors[vertex] = get_available_color(vertex)

        available_colors = ['#' + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)]) for _ in range(self.num_vertices)]
        for vertex, color_index in enumerate(colors):
            color = available_colors[color_index]
            self.node_colors[vertex] = color

@sudoku.route('/visualize', methods=['POST', 'GET'])
def visualize():
    if request.method == 'POST':
        num_vertices = int(request.form['num_vertices'])
        num_edges = int(request.form['num_edges'])

        graph = Graph(num_vertices)
        graph.add_random_edges(num_edges)
        graph.color_graph()
        dot_source = graph.to_dot()
        graphviz_source = Source(dot_source)
        file_name = f".website/static/colored_graph"
        graphviz_source.render(file_name, format='png', cleanup=True)
        return render_template('graph_res.html')

    return render_template('graph.html')
