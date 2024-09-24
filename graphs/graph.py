class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(self.adjacency_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False

    def add_edge(self, vertex1, vertex2):
        graph_list = self.adjacency_list
        if graph_list[vertex1] in graph_list.keys() and graph_list[vertex2] in graph_list.keys():
            graph_list[vertex1].append(vertex2)
            graph_list[vertex2].append(vertex1)
            return True
        return False


my_graph = Graph()
my_graph.add_vertex('a')
my_graph.add_vertex('b')
my_graph.add_edge('a', 'b')
my_graph.add_vertex('c')
my_graph.add_vertex('d')
my_graph.print_graph()
