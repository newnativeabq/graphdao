# oracles.py
from primitives.actions import Action
from primitives.resources import Function, Interface, Actor, Data
from utils.simple_functions import build_read_from_interface


class Oracle(Actor):
    interface: Interface
    data: Data
        
    def collect(self, *args, **kwargs):
        if self.consensus.resolve(*args, **kwargs):
            return self.sign(
                {'data': self.interface.read(*args, **kwargs)}
            )
        
    # Oracles have an associated action.
    #  Register the Action to build the graph
    @property
    def action(self) -> Action:
        return Action(
            identifier=self.identifier,
            resources=[self.interface, self.data],
            function=self.build_oracle_function(),
            actor=self.interface,
        )
    
    def build_oracle_function(self):
        return Function(
            identifier=self.identifier,
            kwargs={'interface': self.interface},
            fn=build_read_from_interface(self.interface)
        )