class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, ':', self.adjacency_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False

    def add_edge(self, vertex1, vertex2):
        graph_list = self.adjacency_list
        if vertex1 in graph_list.keys() and vertex2 in graph_list.keys():
            graph_list[vertex1].append(vertex2)
            graph_list[vertex2].append(vertex1)
            return True
        return False

    def remove_edge(self, vertex1, vertex2):
        adjacency_list = self.adjacency_list
        if vertex1 in adjacency_list.keys() and vertex2 in adjacency_list.keys():
            adjacency_list[vertex1].remove(vertex2)
            adjacency_list[vertex2].remove(vertex1)
            return True
        return False

    def remove_vertex(self, vertex):
        adjacency_list = self.adjacency_list
        if vertex in adjacency_list.keys():
            for other_vertex in adjacency_list[vertex]:
                adjacency_list[other_vertex].remove(vertex)
            # adjacency_list.pop(vertex)
            del adjacency_list[vertex]
            return True
        return False


my_graph = Graph()
my_graph.add_vertex('a')
my_graph.add_vertex('b')
my_graph.add_vertex('c')
my_graph.add_edge('a', 'b')
my_graph.add_edge('b', 'c')
my_graph.remove_edge('a', 'b')
my_graph.remove_vertex('b')
my_graph.add_vertex('d')
my_graph.print_graph()
