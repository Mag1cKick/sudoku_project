from graphviz import Source

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
        self.node_colors = [0] * num_vertices

    def add_edge(self, src, dest):
        self.adjacency_matrix[src][dest] = 1
        self.adjacency_matrix[dest][src] = 1

    def to_dot(self):
        dot_string = "graph G {\n"
        for i in range(self.num_vertices):
            if self.node_colors[i]:
                dot_string += f"    {i} [color={self.node_colors[i]}];\n"

        for i in range(self.num_vertices):
            for j in range(i + 1, self.num_vertices):
                if self.adjacency_matrix[i][j] == 1:
                    dot_string += f"    {i} -- {j};\n"
        dot_string += "}\n"
        return dot_string

    def color_graph(self, num_colors, vertex=0):
        if vertex == self.num_vertices:
            return True

        for color in range(1, num_colors + 1):
            if self.is_safe(vertex, color):
                self.node_colors[vertex] = color
                if self.color_graph(num_colors, vertex + 1):
                    return True
                self.node_colors[vertex] = 0

        return False

    def is_safe(self, v, color):
        for i in range(self.num_vertices):
            if self.adjacency_matrix[v][i] == 1 and self.node_colors[i] == color:
                return False
        return True



if __name__ == "__main__":
    

    # Instantiate the graph
    graph = Graph(5)  # Example: Creating a graph with 5 vertices
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)

    # Color the graph with 3 colors
    graph.color_graph(3)

    # Generate the DOT representation
    dot_representation = graph.to_dot()

    # Visualize the graph
    Source(dot_representation)
