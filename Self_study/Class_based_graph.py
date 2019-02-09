#단순 무향 그래프 구현 시작

class Node():
    neighbor = []
    
    def __init__(self, name):
        self.name = name
        self.degree = 0


    def connect_edge(self, other):
        self.neighbor.append(other)
        self.degree =+ 1

    def get_degree(self):
        return self.degree
    
    def get_neighbor(self):
        return self.neighbor


class Graph():
    nodes = []

    def __init__(self):
        self.num_node = 1
            self.nodes.append(Node(self.num_node))

    def add_node(self, name):
        self.num_node += 1
            self.nodes.append(Node(self.num_node))

    def add_edge(self, start, end):
        self.nodes[start].connect_edge(end)
        self.nodes[end].connect_edge(start)

    def get_node(self, name):
        return self.nodes[name]

    def get_neighbor_of(self, name):
        return self.nodes[name].get_neighbor()

    def get_degree_of(self, name):
        return self.nodes[name].get_degree()
    
    def BFS(start):
        
    def DFS(end):