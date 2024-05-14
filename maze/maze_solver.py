from flask import Flask, request, jsonify, render_template
app = Flask(__name__)


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

@app.route('/', methods = ["GET"])
def index():
    return render_template('maze.html')

@app.route("/maze_solver", methods=["POST"])
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

if __name__ == "__main__":
    app.run(debug=True)
