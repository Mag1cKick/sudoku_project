import random
from graphviz import Source
from flask import Flask, render_template, request

app = Flask(__name__)

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


num_vertices = 5
num_edges = 5
graph = Graph(num_vertices)
graph.add_random_edges(num_edges)
graph.color_graph()
dot_source = graph.to_dot()
graphviz_source = Source(dot_source)
file_name = "./coloring/colored_graph"
graphviz_source.render(file_name, format='png', cleanup=True)
