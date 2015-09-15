import graphviz as gv

def flatten(lol):
    return [item for sublist in lol for item in sublist]

class Graph:
    graph = gv.Graph()
    nodes = []
    edges = []
    
    def add_nodes(self, nodes):
        for n in nodes:
            self.graph.node(n)

    def add_edges(self, edges):
        for e in edges:
            self.graph.edge(*e)
    
    def __init__(self, adjacency):
        parents = adjacency.keys()
        children = adjacency.values()
        self.nodes = set(parents + flatten(children))
        for p in parents:
            for c in adjacency[p]:
                self.edges.append([p, c])
        self.add_nodes(self.nodes)
        self.add_edges(self.edges)

    def render(self, filename):
        self.graph.render(filename, 'pdf', view=True)
