# oracles.py
from typing import List
from queue import SimpleQueue

from primitives.actions import Action
from primitives.resources import Function, Actor, Data
from primitives.interfaces import Interface

from utils.simple_functions import build_read_from_interface
from utils.oracle_helpers import build_oracle_requirements

class Oracle(Actor):
    interface: Interface
    # A limited cache is useful for situations where data will be read 
    #   a known number of times
    cache_reset: int = 1    
    cache = []  

    def cache_data(self, data):
        [self.cache.append(data) for _ in range(self.cache_reset)]

    def read_cache(self):
        if len(self.cache) == 0:
            return False 
        return self.cache.pop()

    def collect(self, *args, **kwargs):
        data = self.read_cache()
        if data:
            return data
        else:
            if self.consensus.resolve(*args, **kwargs):
                data = self.sign(
                    {'data': self.fetch.execute(*args, **kwargs)}
                )
                self.cache_data(data)
                return data
        
    # Oracles have an associated action.
    #  Register the Action and requirements to build the graph
    @property
    def fetch(self) -> Action:
        return Action(
                identifier=self.identifier,
                resources=[self.interface],
                function=self.build_oracle_function(),
                actor=self.interface,
            )

    @property
    def actions(self) -> List[Action]:
        actions = [self.fetch]
        actions.extend(build_oracle_requirements(self))
        return actions
    
    
    def build_oracle_function(self):
        return Function(
            identifier=self.identifier,
            kwargs={'interface': self.interface},
            fn=build_read_from_interface(self.interface)
        )



class ConsensusOracle(Oracle):
    """Consensus Oracle
        Returns signed consensus resolution as data instead of interface read.
    """
    
    def collect(self, *args, **kwargs):
        data = self.sign(
            {'data': self.consensus.resolve(*args, **kwargs)}
        )
        self.cache_data(data)
        return data