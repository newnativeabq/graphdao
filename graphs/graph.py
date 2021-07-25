import networkx as nx

from primitives.actions import Action

class DGraph():
    def __init__(self):
        self.__g = nx.Graph()
        
    def register_action(self, action: Action):
        self.__g.add_nodes_from(action.nodes)
        self.__g.add_edges_from(action.edges)
        print(f"added {action.nodes}, {action.edges}")
        
    @property
    def num_nodes(self):
        return self.__g.number_of_nodes()
    
    @property
    def num_edges(self):
        return self.__g.number_of_edges()
    
    @property
    def nodes(self):
        return self.__g.nodes
    
    @property
    def edges(self):
        return self.__g.edges
    
    def get_edge(self, a, b):
        return self.__g[a][b]
    
    def draw(self, *args, **kwargs):
        nx.draw(self.__g, *args, **kwargs)