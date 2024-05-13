import random
from graphviz import Source

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
        self.node_colors = [None] * num_vertices

    def add_edge(self, src, dest):
        self.adjacency_matrix[src][dest] = 1
        self.adjacency_matrix[dest][src] = 1

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

        # Assign colors to nodes
        available_colors = ['#' + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)]) for _ in range(self.num_vertices)]
        for vertex, color_index in enumerate(colors):
            color = available_colors[color_index]
            self.node_colors[vertex] = color

# Example usage
num_vertices = 5
graph = Graph(num_vertices)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 3)
graph.add_edge(3, 4)

graph.color_graph()

dot_source = graph.to_dot()
graphviz_source = Source(dot_source)
graphviz_source.view()
