class Graph:
    def __init__(self, key=None):
        self.__graph = {}
        if key:
            self.add_vertex(key)

    def add_vertex(self, vertex):
        self.__graph[vertex] = set()

    def add_edge(self, key_one, key_two):
        self.__graph[key_two].add(key_one)
        self.__graph[key_one].add(key_two)

    def find_vertex(self, vertex):
        if self.__graph.get(vertex):
            return True
        return False

    def get_vertices(self):
        return [vertex for vertex in self.__graph.keys()]

    def get_edges(self):
        return [edge for edge in self.__graph.values()]

    def is_adjacent(self, key_one, key_two):
        key_one_edges = self.__graph.get(key_one)
        key_two_edges = self.__graph.get(key_two)
        return key_two in key_one_edges and key_one in key_two_edges

    def get_graph(self):
        return self.__graph


if __name__ == '__main__':
    graph = Graph()
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(11)

    print(f"Current Vertices -> {graph.get_vertices()}")
    print(f"Current Edges: -> {graph.get_edges()}")

    graph.add_edge(4, 5)
    graph.add_edge(5, 11)
    print(f"Current Edges: -> {graph.get_edges()}")

    print(f"Are Vertices 4 & 5 Adjacent -> {graph.is_adjacent(4, 5)}")
    print(f"Are Vertices 4 & 11 Adjacent -> {graph.is_adjacent(4, 11)}")

    print(f"Is 11 A Vertex -> {graph.find_vertex(11)}")
    print(f"Is 41 A Vertex -> {graph.find_vertex(41)}")

