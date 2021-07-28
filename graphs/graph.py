import networkx as nx

from primitives.actions import Action
from primitives.resources import Coalition, Actor
from primitives.oracles import Oracle
from primitives.interfaces import Interface

from utils.coalition_helpers import build_coalition_member_requirements
from utils.actor_helpers import build_actor_consensus_requirements

class DGraph():
    def __init__(self):
        self.__g = nx.Graph()
        
    def register_action(self, action: Action, verbose=False):
        self.__g.add_nodes_from(action.nodes)
        self.__g.add_edges_from(action.edges)
        if verbose:
            print(f"added {action.nodes}, {action.edges}")

    def register_coalition(self, coalition: Coalition, verbose=False):
        actions = build_coalition_member_requirements(coalition)
        for action in actions:
            self.register_action(action, verbose=verbose)

    def register_interface(self, interface: Interface, verbose=False):
        actions = interface.actions
        for action in actions:
            self.register_action(action, verbose=verbose)

    def register_oracle(self, oracle: Oracle, verbose=False):
        actions = oracle.actions
        for action in actions:
            self.register_action(action, verbose=verbose)

    def register_actor(self, actor: Actor, verbose=False):
        actions = build_actor_consensus_requirements(actor)
        for action in actions:
            self.register_action(action, verbose=verbose)

    def compose(self, b):
        self.__g = nx.compose(self.__g, b.graph)
    
    @property
    def graph(self):
        return self.__g

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